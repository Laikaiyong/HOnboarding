<script>
  import { Button, Checkbox, ButtonGroup, Timeline, TimelineItem, Helper, Tabs, TabItem} from 'flowbite-svelte';
  import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
  import * as THREE from 'three';
	import * as SC from 'svelte-cubed';
	import { onMount } from 'svelte';
  import { CheckCircleSolid, VideoSolid, PauseSolid } from 'flowbite-svelte-icons';


</script>

<svelte:head>
	<title>Audio</title>
	<meta name="description" content="Onboard" />
</svelte:head>

<div class="my-1">
  <h2 class='text-4xl font-bold pt-1 pb-3 mb-5 dark:text-white'>Audio Transcript Analysis</h2>

  <Tabs>
    <TabItem open title="Real-time Audio Transcript">
      <div class="grid grid-cols-2 gap-4">
        <div class="col-span-1">
            <Timeline order="vertical">
                <TimelineItem title="Start with a Greeting" date="Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-green-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-green-900">
                      <CheckCircleSolid class="w-3 h-3 text-green-600 dark:text-green-400" />
                    </span>
                  </svelte:fragment>
                  <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Begin the conversation with a warm and professional greeting. Thanks for the call and introduce yourself. </p>
                </TimelineItem>
                <TimelineItem title="Identify the Issue" date="Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-green-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-green-900">
                      <CheckCircleSolid class="w-3 h-3 text-green-600 dark:text-green-400" />
                    </span>
                  </svelte:fragment>
                  <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Inquire about the issue your customer faced.</p>
                </TimelineItem>
                <TimelineItem title="Obtain Customer Details" date="Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-green-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-green-900">
                      <CheckCircleSolid class="w-3 h-3 text-green-600 dark:text-green-400" />
                    </span>
                  </svelte:fragment>
                  <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Verify user identity. Obtain customer name, bank/card account number or other relevant information.</p>
                </TimelineItem>
                <TimelineItem title="Resolve Issue" date="Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-green-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-green-900">
                      <CheckCircleSolid class="w-3 h-3 text-green-600 dark:text-green-400" />
                    </span>
                  </svelte:fragment>
                  <p class="text-base font-normal text-gray-500 dark:text-gray-400">Follow up questions to clarify the issue. Present resolution options, if applicable, and discuss potential solutions. Provide clear and concise information to help the customer make informed decisions.</p>
                </TimelineItem>
                <TimelineItem title="Ask for Confirmation" date="Not Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-gray-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-gray-600">
                      <CheckCircleSolid class="w-3 h-3 text-gray-600 dark:text-gray-400" />
                    </span>
                  </svelte:fragment>
                  <p class="text-base font-normal text-gray-500 dark:text-gray-400">Confirm with the customer whether the provided information or solution meets their needs. This ensures that both parties are on the same page.</p>
                </TimelineItem>
                <TimelineItem title="Thank the Customer" date="Completed">
                  <svelte:fragment slot="icon">
                    <span class="flex absolute -left-3 justify-center items-center w-6 h-6 bg-green-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-green-900">
                      <CheckCircleSolid class="w-3 h-3 text-green-600 dark:text-green-400" />
                    </span>
                  </svelte:fragment>
                  <p class="text-base font-normal text-gray-500 dark:text-gray-400">Express gratitude for the customer's patience and cooperation. Thank them for reaching out and assure them that you value their business.</p>
                </TimelineItem>
              </Timeline>

              <Button pill>Start recording and generate transript</Button>
        </div>
    
        <div class="col-span-1">
          <div class="bg-slate-300 h-20 rounded-xl my-1 p-4">
            <div class="grid grid-cols-5 content-center items-center">
              <div class="col-span-3">
                <div class="flex flex-row-reverse space-x-8 space-x-reverse pr-8">
                  <div>
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 14">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 1H2a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Zm7 11-6-2V4l6-2v10Z"/>
                    </svg>
                  </div>
                  <div>
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 12 18">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1.8c0-.442.32-.8.714-.8h1.429c.394 0 .714.358.714.8v14.4c0 .442-.32.8-.714.8H1.714a.678.678 0 0 1-.505-.234A.851.851 0 0 1 1 16.2V1.8Zm7.143 0c0-.442.32-.8.714-.8h1.429c.19 0 .37.084.505.234.134.15.209.354.209.566v14.4c0 .442-.32.8-.714.8H8.857c-.394 0-.714-.358-.714-.8V1.8Z" clip-rule="evenodd"/>
                    </svg>
                  </div>
                  <div>
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6.143 1H1.857A.857.857 0 0 0 1 1.857v4.286c0 .473.384.857.857.857h4.286A.857.857 0 0 0 7 6.143V1.857A.857.857 0 0 0 6.143 1Zm10 0h-4.286a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286A.857.857 0 0 0 17 6.143V1.857A.857.857 0 0 0 16.143 1Zm-10 10H1.857a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286A.857.857 0 0 0 7 16.143v-4.286A.857.857 0 0 0 6.143 11Zm10 0h-4.286a.857.857 0 0 0-.857.857v4.286c0 .473.384.857.857.857h4.286a.857.857 0 0 0 .857-.857v-4.286a.857.857 0 0 0-.857-.857Z"/>
                    </svg>
                  </div>
                  <div>
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 19">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m9 12 5.419 3.871A1 1 0 0 0 16 15.057V2.943a1 1 0 0 0-1.581-.814L9 6m0 6V6m0 6H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h7m-5 6h3v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-5Zm15-3a3 3 0 0 1-3 3V6a3 3 0 0 1 3 3Z"/>
                    </svg>
                  </div>
                </div>
              </div>
              <div class="col-span-2">
                <Button class="w-full">End Call</Button>
              </div>
            </div>
          </div>
          <div class="border border-2 my-2 p-4 dark:text-white">
            <p class="text-center font-bold dark:text-white mb-3">Conversation Transcript</p>
            <p>Customer: Hi, I'd like to inquire about canceling my credit card.</p>
            <p>Me: Hello! I'm sorry to hear that you're considering canceling your credit card. May I know the reason behind your decision?</p>
            <p>Customer: I've found another card with better rewards, and I think it suits my needs more.</p>
            <p>Me: I see. We value your feedback. Before we proceed, could you please verify some information for security purposes? Can I have your full name and the last four digits of your credit card?</p>
            <p>Customer: Sure, my name is John Doe, and the last four digits are 1234.</p>
            <p>Me: Thank you, John. I've located your account. Now, to better assist you, could you share more details about the new card you're interested in? We might have some options that could match your needs.</p>
            <p>Customer: It's a card with cashback rewards, and I find it more beneficial for my current spending patterns.</p>
            <p>Me: Understood. We appreciate your loyalty, and I'd like to explore any alternatives we may have. Additionally, are there specific features you're looking for in a credit card?</p>
            <p>Customer: I'm mainly interested in a lower annual fee and a solid rewards program.</p>
            <p>Me: Thank you for sharing that, John. We have some options that align with your preferences. Would you be open to discussing these alternatives before making a final decision?</p>
            <p>Customer: Sure, I'm open to hearing about other options.</p>
            <p>Me: Great! Let me provide you with some details on our alternative credit cards that offer competitive rewards and lower annual fees. Please bear with me for a moment.</p>
            <p>Me: John, I've outlined a couple of credit card options that might suit your preferences. Would you like more details on any specific card, or are you still considering cancellation?</p>
            <p>Customer: The alternatives sound interesting. Can you provide more details on the one with the cashback rewards?</p>
            <p>Me: Absolutely, John! The card I have in mind offers cashback on various categories. Here are the key features...</p>
            <p>Me: Does that information help, John? Feel free to ask if you have any questions or if there's anything else you'd like to explore.</p>
            <p>Customer: I appreciate the information. The alternative card seems like a good fit. Let's go ahead and switch to that one.</p>
            <p>Me: Fantastic! I'll initiate the process to switch your card to the new one. You'll receive confirmation shortly. Is there anything else I can assist you with today?</p>
            <p>Customer: No, that covers everything. Thank you for your help!</p>
            <p>Me: You're welcome, John! If you have any further questions in the future, feel free to reach out. Have a great day!</p>
          </div>
        </div>
      </div>
    </TabItem>
    <TabItem title="Upload Audio">
        <iframe title="Bedrock" src="http://localhost:8501/?nav=audio" class="w-[80vw] h-[80vh]" frameborder="0"></iframe>
    </TabItem>
  </Tabs>
</div>