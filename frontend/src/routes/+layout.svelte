<script>
	import Header from './Header.svelte';
	import './styles.css';
  	import "../app.css";
</script>

<div class="app">
	<Header />

	<main class="m-0 p-0">
		<slot />
	</main>

	<!-- <div class="p-4 sm:ml-64">
		<div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">
		   <div class="grid grid-cols-3 gap-4 mb-4">
			  <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
		   </div>
		   <div class="flex items-center justify-center h-48 mb-4 rounded bg-gray-50 dark:bg-gray-800">
			  <p class="text-2xl text-gray-400 dark:text-gray-500">
				 <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
				 </svg>
			  </p>
		   </div>
		   <div class="grid grid-cols-2 gap-4 mb-4">
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
		   </div>
		   <div class="flex items-center justify-center h-48 mb-4 rounded bg-gray-50 dark:bg-gray-800">
			  <p class="text-2xl text-gray-400 dark:text-gray-500">
				 <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
				 </svg>
			  </p>
		   </div>
		   <div class="grid grid-cols-2 gap-4">
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
			  <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
				 <p class="text-2xl text-gray-400 dark:text-gray-500">
					<svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
					   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
					</svg>
				 </p>
			  </div>
		   </div>
		</div>
	 </div> -->

	<footer>
		<p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
