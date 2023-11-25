import streamlit as st
import boto3
from moviepy.editor import *
from PIL import Image
import numpy as np

import os
import json
import base64
from io import BytesIO

title = "Customer Facing"
text1 = "New employees are required to gain an in-depth understanding of anti-money laundering (AML) regulations, Know Your Customer (KYC) procedures, and the bank's adherence to various financial regulations."
text2 = "Onboarding includes training on various account types, loan products, investment options, and digital banking services. This segment ensures that employees are well-equipped to provide accurate and helpful information to clients, fostering trust and loyalty." 
text3 = "Onboarding covers customer service protocols, including effective communication, problem resolution, and maintaining a customer-centric approach. Training in handling sensitive customer information and resolving disputes is also provided to ensure a positive customer experience."


# Create a client object for Amazon Polly
polly_client = boto3.client('polly', region_name='us-east-1')

session = boto3.Session(
    profile_name=os.environ.get("BWB_PROFILE_NAME")
) #sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock-runtime', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
) 

bedrock_model_id = "stability.stable-diffusion-xl-v0" #use the Stable Diffusion model


def get_response_image_from_payload(response): #returns the image bytes from the model response payload

    payload = json.loads(response.get('body').read()) #load the response body into a json object
    images = payload.get('artifacts') #extract the image artifacts
    image_data = base64.b64decode(images[0].get('base64')) #decode image

    return BytesIO(image_data) #return a BytesIO object for client app consumption



def get_image_response(prompt_content): #text-to-text client function
    
    request_body = json.dumps({"text_prompts": 
                               [ {"text": prompt_content } ], #prompts to use
                               "cfg_scale": 9, #how closely the model tries to match the prompt
                               "steps": 50, }) #number of diffusion steps to perform
    
    response = bedrock.invoke_model(body=request_body, modelId=bedrock_model_id) #call the Bedrock endpoint
    
    output = get_response_image_from_payload(response) #convert the response payload to a BytesIO object for the client to consume
    
    return output
    

# Define a function to convert text to speech using Amazon Polly
def convert_to_speech(text, voice):
    polly_client = boto3.client('polly', region_name='us-east-1')
    # text = "<speak><amazon:domain name=\"news\"><amazon:effect name=\"drc\">" + text + "</amazon:effect></amazon:domain></speak>"
    response = polly_client.synthesize_speech(
        Text=text,
        VoiceId=voice,
        OutputFormat='mp3',
        Engine="neural"
    )
    return response['AudioStream'].read()

def autoplay_audio(audio_file):
    b64 = base64.b64encode(audio_file).decode()
    md = f"""
        <audio controls autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(
        md,
        unsafe_allow_html=True,
    )

    # Define a function to create a video from an image and speech
def create_video(image_path, speech, duration):
    clips = [
        ImageClip(
            np.array(Image.open(image_path[0]).convert("RGB"))
        ).set_duration(duration / 2),
        ImageClip(
            np.array(Image.open(image_path[1]).convert("RGB"))
        ).set_duration(duration / 2)
    ]
    oncat_clip = concatenate_videoclips(clips, method="compose")
    oncat_clip.write_videofile('test.mp4', fps=24)
    video_clip = VideoFileClip('test.mp4')
    audio_synthesis = convert_to_speech(speech, 'Joanna')
    with open('test.wav', mode='bw') as f:
        f.write(audio_synthesis)
    
    audio_clip = AudioFileClip("test.wav")
    final= video_clip.set_audio(audio_clip)
    return final


def load_view():
    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:2rem;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)
    text, infographic, audio, video = st.tabs(["💬", "🏞️", "🔊", "📹"])

    with text:
        st.title(title)
        st.write(text1)
        st.write(text2)
        st.write(text3)

    with infographic:
        st.title(title)
        with st.spinner("Drawing..."): #show a spinner while the code in this with block runs
            generated_image = get_image_response(prompt_content=text1) #call the model through the supporting library
            
            st.image(generated_image) 
        st.write(text1)
        st.write(text2)
        with st.spinner("Drawing..."): #show a spinner while the code in this with block runs
            generated_image = get_image_response(prompt_content=text3) #call the model through the supporting library
            
            st.image(generated_image) 
        st.write(text3)

    with audio:
        with st.spinner("Working..."): #show a spinner while the code in this with block runs
            speech = title + ". " + text1 + ". " + text2 + ". " + text3
            audio_clip = convert_to_speech(speech, 'Joanna')
            # st.markdown(f"### [{result['category']}]({result['url']})")
            # st.audio(audio_clip, format='audio/ogg')
            autoplay_audio(audio_clip)
        st.title(title)
        st.write(text1)
        st.write(text2)
        st.write(text3)

    with video:
        with st.spinner("Generating..."): #show a spinner while the code in this with block runs
            generated_image = get_image_response(prompt_content=title) #call the model through the supporting library
            generated_image1 = get_image_response(prompt_content=text2) #call the model through the supporting library
            video = create_video([generated_image, generated_image1], title + ". " + text1 + ". " + text2 + ". " + text3, 20)

            # Save the video as an MP4 file
            video.write_videofile('output.mp4')

            # Display the video
            st.video('output.mp4')

    

