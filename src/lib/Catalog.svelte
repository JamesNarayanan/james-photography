<script lang="ts">
	import { onMount } from "svelte";
	import imageInfo from "../imageInfo.json";
	import type images from "../types/image";

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
			<img src={imageInfo.src} alt={imageInfo.description} />
		{/each}
	{:else}
		<div class="loading">Loading...</div>
	{/if}
</div>
