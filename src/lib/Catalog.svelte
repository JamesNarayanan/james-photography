<script lang="ts">
	import { onMount } from "svelte";
	import imageInfo from "../imageInfo.json";
	import type { images } from "../types/image";
	import CatalogImage from "./CatalogImage.svelte";

	const imagesInfo: images = {};

	onMount(() => {
		const imageModules = import.meta.glob("../assets/thumbs/*.jpeg");

		for (const modulePath in imageModules) {
			imageModules[modulePath]().then(({ default: imageUrl }) => {
				const imageNameSegments = imageUrl.split("/");
				const imageName = imageNameSegments[imageNameSegments.length - 1];

				imagesInfo[imageName] = {
					thumb: imageUrl,
					fullsize: imageUrl.replace("thumbs", "fullsize"),
					...imageInfo[imageName]
				};
			});
		}

		// Get the exif metadata for the images on window load
		window.onload = getData;
		function getData() {
			const images = document.getElementsByTagName("img");
			const EXIF = (window as any).EXIF;
			for (var i = 0; i < images.length; i++) {
				const details = images[i];
				const imageNameSegments = details.currentSrc.split("/");
				const imageName = imageNameSegments[imageNameSegments.length - 1];
				EXIF.getData(images[i], function () {
					var allMetaData = EXIF.getAllTags(this);
					imagesInfo[imageName].exif = allMetaData;
				});
			}
		}
	});
</script>

<div class="catalog">
	{#if Object.keys(imagesInfo).length > 0}
		{#each Object.values(imagesInfo) as imageInfo}
			<CatalogImage {imageInfo} />
		{/each}
	{:else}
		<div class="loading">Loading...</div>
	{/if}
</div>
