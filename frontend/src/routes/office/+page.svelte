<script>
    import {
		Button
	} from 'flowbite-svelte';
    var tourStart = false;

    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
    import * as THREE from 'three';
	import * as SC from 'svelte-cubed';
	import { onMount } from 'svelte';

    let spin = 0;
    let width = 0.1;
    let height = 0.1;
    let depth = 0.1;

	SC.onFrame(() => {
		spin+= 0.001;
	});

    let model;
    onMount(async () => {
        model = (await new GLTFLoader().loadAsync("https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/RobotExpressive/RobotExpressive.glb")).scene
    })
</script>

<svelte:head>
	<title>Office</title>
	<meta name="description" content="Office Tour" />
</svelte:head>

<div class="ml-10">
    <Button on:click={() => tourStart = !tourStart}>
        Toggle Other Condition
    </Button>
    
    {#if tourStart}
        <iframe class="mx-[10vw] w-[80vw] lg:mx-0 h-[70vh]" allowfullscreen title="Office Tour" style="border-style:none;" src="https://cdn.pannellum.org/2.4/pannellum.htm#config=https://raw.githubusercontent.com/Laikaiyong/Cpp-Labs/main/tour.json&amp;autoLoad=true"></iframe>
    {:else}
        <div class="mt-[20vh]"></div>
        <SC.Canvas
            antialias
            background={new THREE.Color('papayawhip')}
    	    fog={new THREE.FogExp2('papayawhip', 0.1)}
            shadows
        >
            {#if model}
                <SC.Primitive object={model} scale={[width, height, depth]} rotation={[0, spin, 0]}
                />
            <!-- {:else}
            <SC.Mesh
                geometry={new THREE.BoxGeometry()}
                material={new THREE.MeshStandardMaterial({ color: 0xff3e00 })}
                scale={[width, height, depth]}
                rotation={[0, spin, 0]}
                castShadow
            /> -->
            {/if}
            <SC.PerspectiveCamera position={[1, 1, 3]} />
            <SC.OrbitControls enableZoom={false} maxPolarAngle={Math.PI * 0.51} />
            <SC.AmbientLight intensity={0.6} />
	        <SC.DirectionalLight intensity={0.6} position={[-2, 3, 2]} shadow={{ mapSize: [2048, 2048] }} />
            <SC.Group position={[0, - 1 / 2, 0]}>
                <SC.Mesh
                    geometry={new THREE.PlaneGeometry(50, 50)}
                    material={new THREE.MeshStandardMaterial({ color: 'burlywood' })}
                    rotation={[-Math.PI / 2, 0, 0]}
                    receiveShadow
                />
            
                <SC.Primitive
                    object={new THREE.GridHelper(50, 50, 0x444444, 0x555555)}
                    position={[0, 0.001, 0]}
                />
            </SC.Group>
        </SC.Canvas>
    {/if}
</div>


<style>
</style>