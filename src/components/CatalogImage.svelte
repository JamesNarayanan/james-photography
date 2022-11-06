<script lang="ts">
	import { onMount } from "svelte";
	import type { image } from "../types/image";
	import ApertureIcon from "../assets/icons/ApertureIcon.svelte";
	import CameraIcon from "../assets/icons/CameraIcon.svelte";
	import FocalLengthIcon from "../assets/icons/FocalLengthIcon.svelte";
	import IsoIcon from "../assets/icons/IsoIcon.svelte";
	import LocationIcon from "../assets/icons/LocationIcon.svelte";
	import ShutterSpeedIcon from "../assets/icons/ShutterSpeedIcon.svelte";

	export let imageInfo: image;

	let focused: boolean = false;
	let imageWrapper: HTMLDivElement;
	let imageHoverScale: number;

	onMount(() => {
		imageHoverScale = parseFloat(
			getComputedStyle(document.documentElement).getPropertyValue("--image-hover-scale")
		);
	});
	function handleMouseEnter(event: MouseEvent) {
		if (focused) return;

		document.getElementsByClassName("cursor")[0].classList.add("object-hover");
		const rect = imageWrapper.getBoundingClientRect();
		const x = rect.left + rect.width / 2;
		const y = imageWrapper.offsetTop + rect.height / 2;
		const width = rect.width * imageHoverScale;
		const height = rect.height * imageHoverScale;
		document.documentElement.style.setProperty("--selected-x", x + "px");
		document.documentElement.style.setProperty("--selected-y", y + "px");
		document.documentElement.style.setProperty("--cursor-width", width + "px");
		document.documentElement.style.setProperty("--cursor-height", height + "px");
	}
	function handleMouseExit() {
		if (focused) return;

		document.getElementsByClassName("cursor")[0].classList.remove("object-hover");
		document.documentElement.style.setProperty("--cursor-width", "var(--default-cursor-size)");
		document.documentElement.style.setProperty("--cursor-height", "var(--default-cursor-size)");
	}
	function handleClick() {
		if (!focused) {
			focused = true;
			document.getElementsByClassName("cursor")[0].classList.remove("object-hover");
			document.documentElement.style.setProperty("--cursor-width", "var(--default-cursor-size)");
			document.documentElement.style.setProperty("--cursor-height", "var(--default-cursor-size)");
		}
	}
</script>

<div class={`image-container-outer ${focused ? "focused" : ""}`} bind:this={imageWrapper}>
	<div class="image-container-inner">
		<img
			src={imageInfo.fullsize}
			alt={imageInfo.description}
			on:mouseenter={handleMouseEnter}
			on:mouseleave={handleMouseExit}
			on:click={handleClick}
		/>
		<div class="image-overlay">
			<div class="top">
				<button class="x" on:click={() => (focused = false)}>&times;</button>
				<div class="detail"><LocationIcon /> {imageInfo.location}</div>
			</div>
			{#if imageInfo.exif}
				<div class="bottom">
					<div class="detail">
						<CameraIcon />
						{imageInfo.exif.Make}
						{imageInfo.exif.Model}
					</div>
					<div class="detail">
						<FocalLengthIcon />
						{imageInfo.exif.FocalLength}mm
					</div>
					<div class="detail">
						<ApertureIcon />
						<div>
							<i>f</i>/{imageInfo.exif.FNumber}
						</div>
					</div>
					<div class="detail">
						<ShutterSpeedIcon />
						{#if imageInfo.exif.ExposureTime < 1}
							{imageInfo.exif.ExposureTime.numerator}/{imageInfo.exif.ExposureTime.denominator}s
						{:else}
							{imageInfo.exif.ExposureTime}s
						{/if}
					</div>
					<div class="detail">
						<IsoIcon />
						{imageInfo.exif.ISOSpeedRatings}
					</div>
				</div>
			{/if}
		</div>
	</div>
</div>
