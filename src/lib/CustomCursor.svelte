<script lang="ts">
	import "../scss/cursor.scss";

	let cursor: HTMLElement;

	function handleMouseMove(event: MouseEvent) {
		cursor.style.left = `${event.clientX}px`;
		cursor.style.top = `${event.clientY}px`;
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
