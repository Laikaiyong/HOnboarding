const config = {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'
	],

	theme: {
		extend: {
			colors: {
				// flowbite-svelte
				primary: {
					50: '#EF392C',
					100: '#EF392C',
					200: '#EF392C',
					300: '#EF392C',
					400: '#EF392C',
					500: '#EF392C',
					600: '#EF392C',
					700: '#EF392C',
					800: '#EF392C',
					900: '#EF392C'
				},
				secondary: {
					50: '#081E4E',
					100: '#081E4E',
					200: '#081E4E',
					300: '#081E4E',
					400: '#081E4E',
					500: '#081E4E',
					600: '#081E4E',
					700: '#081E4E',
					800: '#081E4E',
					900: '#081E4E'
				}
			}
		}
	},

	plugins: [require('flowbite/plugin')],
	darkMode: 'class'
};

module.exports = config;
