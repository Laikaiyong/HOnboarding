<script lang="ts">
	import '../app.css';
	import type { PageData } from './$types';
	import { page } from '$app/stores';
	import { SvelteComponent, onMount } from 'svelte';
	import {
		P,
		Hr,
		Button,
		DarkMode,
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Search,
		Sidebar,
		SidebarGroup,
		SidebarItem,
		SidebarWrapper,
		Drawer,
		CloseButton,
		SidebarDropdownWrapper
	} from 'flowbite-svelte';
	import * as Icons from 'flowbite-svelte-icons';
	import { Cog } from 'svelte-heros-v2';
	import { sineIn } from 'svelte/easing';

	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn
	};
	export let data: PageData;

	let breakPoint: number = 1024;
	let width: number;
	let backdrop: boolean = false;
	let activateClickOutside = true;
	let drawerHidden: boolean = false;
	$: if (width >= breakPoint) {
		drawerHidden = false;
		activateClickOutside = false;
	} else {
		drawerHidden = true;
		activateClickOutside = true;
	}
	onMount(() => {
		if (width >= breakPoint) {
			drawerHidden = false;
			activateClickOutside = false;
		} else {
			drawerHidden = true;
			activateClickOutside = true;
		}
	});
	const toggleSide = () => {
		if (width < breakPoint) {
			drawerHidden = !drawerHidden;
		}
	};
	const toggleDrawer = () => {
		drawerHidden = false;
	};
	$: activeUrl = $page.url.pathname;
	let spanClass = 'pl-2 self-center text-md text-white whitespace-nowrap';
	let divClass = 'w-full ml-auto lg:block lg:w-auto order-1 lg:order-none';
	let ulClass =
		'flex flex-col py-3 my-4 lg:flex-row lg:my-0 text-sm font-medium gap-4 dark:lg:bg-transparent lg:bg-white lg:border-0';
	let navDivClass =
		'bg-white dark:bg-gray-800 text-gray-500 dark:text-gray-400 border-gray-200 dark:border-gray-700 divide-gray-200 dark:divide-gray-700 flex items-center justify-between w-full mx-auto py-1.5 px-4';
</script>

<svelte:window bind:innerWidth={width} />
<header class="flex-none w-full mx-auto dark:bg-slate-950">
	<Navbar let:hidden let:toggle>
		<NavHamburger
			on:click={toggleDrawer}
			btnClass="focus:outline-none whitespace-normal rounded-lg focus:ring-2 p-1.5 focus:ring-gray-400 hover:bg-gray-100 dark:hover:bg-gray-600 m-0 mr-3 lg:hidden"
		/>
		<NavBrand href="/pages/0_home" class="lg:ml-64">
			<img class="h-10" src="/images/honboarding-logo.png" alt="HOnboarding Logo"/>
			<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white pl-4">
				HOnBoarding
			</span>
		</NavBrand>
		<div class="flex items-center ml-auto">
			<DarkMode class="inline-block dark:hover:text-white hover:text-gray-900" />
		</div>
		<!-- <NavHamburger on:click={toggle} btnClass="lg:hidden" /> -->
		<NavUl>
			<!-- <Search>
				<Button>Search</Button>
			</Search> -->
			<NavLi href="/notifications">Notifications</NavLi>
			<NavLi href="/alerts">Alerts</NavLi>
			<NavLi href="/settings">Settings</NavLi>
			<NavLi href="/profile">Profile</NavLi>
    	</NavUl>
	</Navbar>
</header>

<Drawer
	transitionType="fly"
	{backdrop}
	{transitionParams}
	bind:hidden={drawerHidden}
	bind:activateClickOutside
	width="w-64"
	class="overflow-scroll pb-32 bg-secondary-50 text-white dark:bg-secondary-50 dark:bg-opacity-40"
	id="sidebar"
>
	<div class="flex items-center">
		<CloseButton on:click={() => (drawerHidden = true)} class="mb-4 dark:text-white lg:hidden" />
	</div>
	<Sidebar asideClass="w-54">
		<SidebarWrapper divClass="overflow-y-auto py-4 px-3 rounded">
			<SidebarGroup>
				<SidebarItem
					label="Home"
					href={`/home`}
					{spanClass}
					class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
					activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
					on:click={toggleSide}
					active={activeUrl === `/home`}
				>
					<svelte:fragment slot="icon">
						<svelte:component this={Icons.HomeSolid} class="text-white"/>
					</svelte:fragment>
				</SidebarItem>

				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="re:Onboard">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons.UsersSolid}/>
					  	</svelte:fragment>
						<SidebarItem
							label="E-Sensei"
							href={`/onboard`}
							{spanClass}
							class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
							activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
							on:click={toggleSide}
							active={activeUrl === `/onboard`}
						>
							<svelte:fragment slot="icon">
								<svelte:component this={Icons.LifeBuoySolid} class="text-white"/>
							</svelte:fragment>
						</SidebarItem>
						
						<SidebarItem
							label="Chat"
							href={`/chat`}
							{spanClass}
							class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
							activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
							on:click={toggleSide}
							active={activeUrl === `/chat`}
						>
							<svelte:fragment slot="icon">
								<svelte:component this={Icons.MessagesSolid} class="text-white"/>
							</svelte:fragment>
						</SidebarItem>
						
						<SidebarItem
							label="Audio"
							href={`/audio`}
							{spanClass}
							class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
							activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
							on:click={toggleSide}
							active={activeUrl === `/audio`}
						>
							<svelte:fragment slot="icon">
								<svelte:component this={Icons.VolumeUpSolid} class="text-white"/>
							</svelte:fragment>
						</SidebarItem>
				</SidebarDropdownWrapper>

				<SidebarItem
					label="Office Tour"
					href={`/office`}
					{spanClass}
					class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
					activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
					on:click={toggleSide}
					active={activeUrl === `/office`}
				>
					<svelte:fragment slot="icon">
						<svelte:component this={Icons.BuildingSolid} class="text-white"/>
					</svelte:fragment>
				</SidebarItem>

				<SidebarItem
					label="Schedule"
					href={`/schedule`}
					{spanClass}
					class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
					activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
					on:click={toggleSide}
					active={activeUrl === `/schedule`}
				>
					<svelte:fragment slot="icon">
						<svelte:component this={Icons.BriefcaseSolid} class="text-white"/>
					</svelte:fragment>
				</SidebarItem>
				<Hr />
				
				<P size="2xl" class="text-white">Knowledge Base</P>
				<SidebarItem
					label="Search"
					href={`/search`}
					{spanClass}
					class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
					activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
					on:click={toggleSide}
					active={activeUrl === `/search`}
				>
					<svelte:fragment slot="icon">
						<svelte:component this={Icons.SearchSolid} class="text-white"/>
					</svelte:fragment>
				</SidebarItem>

				<SidebarItem
					label="Study Mode"
					href={`/study`}
					{spanClass}
					class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
					activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
					on:click={toggleSide}
					active={activeUrl === `/study`}
				>
					<svelte:fragment slot="icon">
						<svelte:component this={Icons.OpenBookSolid} class="text-white"/>
					</svelte:fragment>
				</SidebarItem>

				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="Company">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons["BookSolid"]}/>
					  	</svelte:fragment>
						  <SidebarItem
						  label="Overview"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Org Structure"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Policies"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Responsibilities"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Diversify"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Compliance"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
				</SidebarDropdownWrapper>

				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="Supports">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons["BookSolid"]}/>
					  	</svelte:fragment>
						  <SidebarItem
						  label="Benefits"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Leaves"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Training"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Tools"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Health"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="EAP"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
				</SidebarDropdownWrapper>


				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="Channels">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons["BookSolid"]}/>
					  	</svelte:fragment>
						  <SidebarItem
						  label="Communication"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Expectations"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						 
				</SidebarDropdownWrapper>


				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="Culture">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons["BookSolid"]}/>
					  	</svelte:fragment>
						  <SidebarItem
						  label="Environment"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Recognition"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						 
				</SidebarDropdownWrapper>


				<SidebarDropdownWrapper class="hover:bg-primary-200 hover:text-white hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10 text-white" label="Engagement">

					<svelte:fragment slot="icon">
							<svelte:component this={Icons["BookSolid"]}/>
					  	</svelte:fragment>
						  <SidebarItem
						  label="Bonding"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Contact"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="Feedback"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						  <SidebarItem
						  label="FAQs"
						  {spanClass}
						  class="hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:hover:bg-white dark:hover:text-black dark:hover:bg-opacity-10"
						  activeClass="flex items-center p-2 font-normal bg-primary-600 dark:bg-primary-700 rounded-lg text-white hover:bg-primary-200 hover:text-black hover:bg-opacity-700 dark:bg-opacity-25 bg-opacity-50"
						  on:click={toggleSide}
					  >
						  <svelte:fragment slot="icon">
							  <svelte:component this={Icons.BookmarkSolid} class="text-white"/>
						  </svelte:fragment>
					  </SidebarItem>
						 
				</SidebarDropdownWrapper>
			</SidebarGroup>
		</SidebarWrapper>
	</Sidebar>
</Drawer>

<div class="flex px-4 mx-auto w-full">
	<main class="lg:ml-72 w-full mx-auto">
		<slot />
	</main>
</div>
