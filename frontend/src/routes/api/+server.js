import { json } from '@sveltejs/kit';
// import { OPENAI_API_SECRET_KEY } from '';

export const GET = async () => {
	const allPosts = await fetchMarkdownPosts();
	return json(allPosts);
};

const fetchMarkdownPosts = async () => {
	const spaceFiles = import.meta.glob('/src/routes/spaces/*.md');
	const pageFiles = import.meta.glob('/src/routes/pages/*.md');
	const svelteFiles = import.meta.glob('/src/routes/svelte/*.svelte');
	const searchFile = import.meta.glob('/src/routes/searchalone/*.svelte');


	// returns an array of files
	const iterableSpaceFiles = Object.entries(spaceFiles);
	const iterablePageFiles = Object.entries(pageFiles);
	const iterableSvelteFiles = Object.entries(svelteFiles);
	const iterableSearchFile = Object.entries(searchFile);

	const search = await Promise.all(
		iterableSearchFile.map(async ([path, resolver]) => {
			const { metadata } = await resolver();
			const filePath = path.slice(24, -3);
			console.log(filePath);
			return {
				meta: metadata,
				path: filePath
			};
		})
	);

	const spaces = await Promise.all(
		iterableSpaceFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver();
			const filePath = path.slice(19, -3);
			return {
				meta: metadata,
				path: filePath
			};
		})
	);

	const pages = await Promise.all(
		iterablePageFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver();
			const filePath = path.slice(18, -3);
			return {
				meta: metadata,
				path: filePath
			};
		})
	);

	const sveltefiles = await Promise.all(
		iterableSvelteFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver();
			const filePath = path.slice(18, -7);
			return {
				meta: metadata,
				path: filePath
			};
		})
	);

	return { pages, spaces,  search, sveltefiles };
};
