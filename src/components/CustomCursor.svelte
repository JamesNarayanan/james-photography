<script lang="ts">
	import ZoomInIcon from "../assets/icons/ZoomInIcon.svelte";
	import "../scss/cursor.scss";

	let cursor: HTMLElement;

	function handleMouseMove(event: MouseEvent) {
		document.documentElement.style.setProperty("--cursor-x", event.clientX + "px");
		document.documentElement.style.setProperty("--cursor-y", event.clientY + "px");
	}
	function handleMouseDown() {
		cursor.classList.add("down");
	}
	function handleMouseUp() {
		cursor.classList.remove("down");
	}
</script>

<svelte:window on:mousemove={handleMouseMove} on:mousedown={handleMouseDown} on:mouseup={handleMouseUp} />
<div class="cursor" bind:this={cursor} />
<div class="cursor-inner default" />
<div class="cursor-inner zoom-in"><ZoomInIcon className="invert-icon" /></div>
