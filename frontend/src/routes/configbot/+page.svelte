<script lang="ts">
    import { Avatar, Dropdown, DropdownHeader, DropdownItem, DropdownDivider, Tooltip, Label, Input,Textarea} from 'flowbite-svelte';
    import { Button } from 'flowbite-svelte';
    import { ChevronDownSolid } from 'flowbite-svelte-icons';
    import { Fileupload, Helper, Checkbox } from 'flowbite-svelte';
    let textareaprops = {
    id: 'message',
    name: 'message',
    label: 'Your message',
    rows: 4,
    placeholder: 'Description'
  };
</script>

<svelte:head>
	<title>Chatbot Configuration</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div>
    <h1 class='text-4xl font-bold pt-1 pb-0 dark:text-white'>Configure Chatbot</h1><br>
    <h4 class='text-lg font-normal pt-0 pb-3 dark:text-white'>Configure your chatbot to retieve information more effectively</h4>
</div>

<div class="bot"><Avatar size="xl" border /></div>
<div class="details">
	<div>
		<Label for="Name" class="block mb-2">Name</Label>
		<Input id="Name" placeholder="Bot 1" />
	</div>

	<div class="mt-5">
		<Label for="Description" class="block mb-2">Description</Label>
		<Textarea {...textareaprops} />
	</div>

	<div class="mt-5">
		<Label for="Language" class="block mb-2">Language</Label>
		<Button color="red">Language<ChevronDownSolid class="w-3 h-3 ml-2 text-white dark:text-white" /></Button>
		<Dropdown>
		<DropdownItem>English</DropdownItem>
		<DropdownItem>Bahasa Malaysia</DropdownItem>
		<DropdownItem>中文</DropdownItem>
		<DropdownItem>Others</DropdownItem>
		</Dropdown>
	</div>

	<div class="mt-5">
		<Label for="with_helper" class="pb-2">Upload Document</Label>
		<Fileupload id="with_helper" class="mb-2" />
		<Helper> .pdf, .doc, .txt (MAX 10MB). </Helper>
	</div>

	<div class="mt-5"><Label for="Knowledge" class="block mb-2">Knowledge Base</Label>
		<div class="rounded border border-gray-200 dark:border-gray-700">
			<Checkbox class="w-full p-4">Company</Checkbox>
		</div>
		<div class="rounded border border-gray-200 dark:border-gray-700">
			<Checkbox checked class="w-full p-4">Supports</Checkbox>
		</div>
		<div class="rounded border border-gray-200 dark:border-gray-700">
			<Checkbox checked class="w-full p-4">Channels</Checkbox>
		</div>
        <div class="rounded border border-gray-200 dark:border-gray-700">
			<Checkbox checked class="w-full p-4">Culture</Checkbox>
		</div>
        <div class="rounded border border-gray-200 dark:border-gray-700">
			<Checkbox checked class="w-full p-4">Engagement</Checkbox>
		</div>
	</div>
	<div class="mt-2 ml-4 mb-8">
		<Button class="button1 w-20"outline color="blue">Save</Button>
		<Button class="button2 w-20 ml-4"outline color="red">Delete</Button>
	</div>
</div>


<style>
     .bot {
		margin-top: 12px;
        width: 100px;
        float: left; 
        flex: 1;
        }  
      .details {
		margin-top: 12px;
        width: 80%;
        float: left; 
        flex: 1;
        margin-left: 100px;
        }
</style>