/**
 * Svelte configuration for the Tailspin Toys Crowd Funding platform.
 * This module configures Svelte preprocessing for the Astro integration.
 */
import { vitePreprocess } from '@astrojs/svelte';

export default {
	preprocess: vitePreprocess(),
}
