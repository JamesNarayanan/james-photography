<script lang="ts">
	import { onMount } from "svelte";
	import type { image } from "../types/image";

	export let imageName: string;
	export let imageInfo: image;

	let image: HTMLImageElement;
	let imageHoverScale: number;

	onMount(() => {
		imageHoverScale = parseFloat(
			getComputedStyle(document.documentElement).getPropertyValue("--image-hover-scale")
		);
	});
	function handleMouseEnter(event: MouseEvent) {
		document.getElementsByClassName("cursor")[0].classList.add("object-hover");
		const rect = image.getBoundingClientRect();
		const x = rect.left + rect.width / 2;
		const y = rect.top + rect.height / 2;
		const width = rect.width * imageHoverScale;
		const height = rect.height * imageHoverScale;
		document.documentElement.style.setProperty("--selected-x", x + "px");
		document.documentElement.style.setProperty("--selected-y", y + "px");
		document.documentElement.style.setProperty("--cursor-width", width + "px");
		document.documentElement.style.setProperty("--cursor-height", height + "px");
	}
	function handleMouseExit() {
		document.getElementsByClassName("cursor")[0].classList.remove("object-hover");
		document.documentElement.style.setProperty("--cursor-width", "var(--default-cursor-size)");
		document.documentElement.style.setProperty("--cursor-height", "var(--default-cursor-size)");
	}
</script>

<img
	src={imageInfo.thumb}
	alt={imageInfo.description}
	bind:this={image}
	on:mouseenter={handleMouseEnter}
	on:mouseleave={handleMouseExit}
/>
