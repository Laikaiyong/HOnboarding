<script lang="ts">
    import { Tooltip, Img, Button, Dropdown, DropdownItem, Radio, Hr, Range, Label, P, Layout } from 'flowbite-svelte';
    import { ChevronDownSolid } from 'flowbite-svelte-icons';

    let minmaxValue = 5;

    let snsIntegrationList = [
		{ id: '0', name: 'Messenger', src: "/images/messenger.png" },
		{ id: '1', name: 'Whatsapp', src: '/images/whatsapp.png'},
		{ id: '2', name: 'Telegram', src: '/images/telegram.png' },
        { id: '3', name: 'Instagram', src: '/images/instagram.png'}
	];

    let sampleChat = [
        {role: 'user', message: 'Hi'},
        {role: 'assistant', message: 'Hi there! How may I help you?'},
        {role: 'user', message: 'May I get the list of ongoing promotions in the 4th quarter of 2023? '},
        {role: 'assistant', message: 'Sure! Here it is'},
        {role: 'user', message: 'May I get the list of ongoing promotions in the 4th quarter of 2023? '},
        {role: 'assistant', message: 'Sure! Here it is'},
        {role: 'user', message: 'May I get the list of ongoing promotions in the 4th quarter of 2023? '},
        {role: 'assistant', message: 'Sure! Here it is'},
    ];
    
</script>

<svelte:head>
	<title>Chat</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="m-2">
    <h1 class='text-4xl font-bold pt-1 pb-0 dark:text-white'>Chat</h1>
    <h4 class='text-lg font-normal pt-0 pb-3 dark:text-white'>Empower Your Customer Interactions with a Personalized Chat Support</h4>
    <div class='border-2 py-2 px-4 rounded-lg mb-2'>
        <div class="flex flex-row items-center content-center">
            <div>
                <h3 class='pt-2 pb-3 dark:text-white'>Customer Chatbot Integrations</h3>
                
            </div>
            <div class="px-4">
                <button>
                    <svg class="w-4 h-4 text-gray-400 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm0 16a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3Zm1-5.034V12a1 1 0 0 1-2 0v-1.418a1 1 0 0 1 1.038-.999 1.436 1.436 0 0 0 1.488-1.441 1.501 1.501 0 1 0-3-.116.986.986 0 0 1-1.037.961 1 1 0 0 1-.96-1.037A3.5 3.5 0 1 1 11 11.466Z"/>
                    </svg>
                </button>
                <Tooltip>Tooltip content placeholder</Tooltip>
            </div>
        </div>
        <div class='flex-row inline-flex items-center'>
            <div>
                {#each snsIntegrationList as { name, src }}
                <label class="relative inline-flex items-center cursor-pointer">
                    <!-- <picture class="h-8 mb-3 align-middle">
                    <source srcset={Messenger_logo} type="image/webp" />
                    <img src={Messenger_logo} class="h-8 mb-3 mx-3 mt-1"  alt="HOnboarding Logo"/>
                </picture> -->
                    <img class="h-10 pr-2" src={src} alt={name}/>
                    <label class="relative inline-flex items-center cursor-pointer pr-6">
                        <input type="checkbox" value="" class="sr-only peer">
                        <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                    </label>
                </label>
                {/each}
            </div>
            <div class="flex justify-end">
                <div>
                    <Button href="/configbot" class="" color="red">Configure</Button>
                </div>
            </div>
        </div>
    </div>
    <Hr />
    <h2 class='text-2xl font-bold pt-2 pb-2 dark:text-white'>Hong Leong Bot</h2>
<!--     
    <div class='flex flex-row h-full'>
        <div class='basis-1/2 xs:basis-0'>
            <Label class="mt-5 text-base dark:text-white">Conversation Style</Label>
            <Range id="range-minmax" min="0" max="10" bind:value={minmaxValue} />
            <div class="grid grid-cols-3 gap-3"> 
                <div> 
                    <p class="text-left dark:text-white p-1">Casual</p> 
                </div> 
                <div> 
                    <p class="text-center dark:text-white p-1">Value: {minmaxValue}</p> 
                </div> 
                <div> 
                    <p class="text-right dark:text-white p-1">Professional</p> 
                </div> 
                
                
                <Button class=" bg-[#081E4E]  dark:bg-[#1338bf]">Chatbot Role<ChevronDownSolid class="w-3 h-3 ml-3 text-white dark:text-white" /></Button>
                <Dropdown>
                <DropdownItem>Marketing Personnel</DropdownItem>
                <DropdownItem>Technical Advisor</DropdownItem>
                <DropdownItem>Legal Advisor</DropdownItem>
                <DropdownItem>HR Manager</DropdownItem>
                </Dropdown>
                      
    
                <div>        
                <p class="mb-1 font-semibold text-gray-900 dark:text-white">Output</p>
                <ul class="items-center w-full rounded-lg border border-gray-300 sm:flex dark:bg-gray-800 dark:border-gray-600 divide-x divide-gray-300 dark:divide-gray-600">
                <li class="w-full"><Radio name="hor-list" class="p-3">PDF</Radio></li>
                <li class="w-full"><Radio name="hor-list" class="p-3">Image</Radio></li>
                <li class="w-full"><Radio name="hor-list" class="p-3">Text</Radio></li>
                </ul>
                </div>
            </div>
        </div> -->

        <!-- Chatbot starts here -->
        <!-- <div class='basis-1/2 xs:basis-1/1'>
            <div class="m-4">
                <div class="w-full  text-center rounded-t-lg p-4 bg-[#081E4E] dark:bg-[#1338bf]">
                    <h1 class="text-xl font-bold pt-1 pb-0 text-white">Chatbot</h1>
                </div>
                <div class="h-full max-h-lg flex flex-col bg-gray-200 dark:bg-gray-700 overflow-x-hidden overflow-y-auto">
                    {#each sampleChat as {role,message}}
                    {#if role=='user'}
                        <div class="mx-4 my-2 flex justify-end">
                            <div class="max-w-md">
                                <p class="text-white dark:text-white px-4 py-2 bg-[#081E4E] dark:bg-[#1338bf] rounded-2xl">{message}</p>
                            </div>
                        </div>
                    {:else if role=='assistant'}
                        <div class="mx-4 my-2 flex justify-start">
                            <div class="max-w-md">
                                <p class="text-black dark:text-black px-4 py-2 bg-white rounded-2xl">{message}</p>
                            </div>
                        </div>
                    {/if}
                    {/each}
                </div>
                <div class="bottom-0 items-center content-center">
                    <div>
                    <form >
                        <label for="chat" class="sr-only">Your message</label>
                        <div class="w-full flex items-center px-2 py-2 rounded-b-lg bg-gray-200 dark:bg-gray-700">
                            <button type="button" class="inline-flex justify-center p-2 text-gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 18">
                                    <path fill="currentColor" d="M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z"/>
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 1H2a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z"/>
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z"/>
                                </svg>
                                <span class="sr-only">Upload image</span>
                            </button>
                            <button type="button" class="p-2 text-dark gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.408 7.5h.01m-6.876 0h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM4.6 11a5.5 5.5 0 0 0 10.81 0H4.6Z"/>
                                </svg>
                                <span class="sr-only">Add emoji</span>
                            </button>
                            <textarea id="chat" rows="1" class="block mx-4 p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Your message..."></textarea>
                                <button type="submit" class="inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600">
                                <svg class="w-5 h-5 rotate-90 rtl:-rotate-90" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                                    <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                                </svg>
                                <span class="sr-only">Send message</span>
                            </button>
                        </div>
                    </form>
                    </div>
                </div>
            </div>
        </div> -->

    <!-- </div> -->
    <iframe title="Bedrock" src="http://localhost:8501/?nav=email" class="w-[80vw] h-[80vh]" frameborder="0"></iframe>
</div>