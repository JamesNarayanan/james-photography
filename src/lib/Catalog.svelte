<script lang="ts">
	import { onMount } from "svelte";
	import imageInfo from "../imageInfo.json";
	import type { images } from "../types/image";
	import CatalogImage from "./CatalogImage.svelte";

	const imagesInfo: images = {};

	onMount(() => {
		const imageModules = import.meta.glob("../assets/*.jpeg");

		for (const modulePath in imageModules) {
			imageModules[modulePath]().then(({ default: imageUrl }) => {
				const imageNameSegments = imageUrl.split("/");
				const imageName = imageNameSegments[imageNameSegments.length - 1];

				imagesInfo[imageName] = {
					src: imageUrl,
					...imageInfo[imageName]
				};
			});
		}
	});
</script>

<div class="catalog">
	{#if Object.keys(imagesInfo).length > 0}
		{#each Object.entries(imagesInfo) as [imageName, imageInfo]}
			<CatalogImage {imageName} {imageInfo} />
		{/each}
	{:else}
		<div class="loading">Loading...</div>
	{/if}
</div>
