<script>
    import {
		Button
	} from 'flowbite-svelte';
    var panaroma = false;
    var tourStart = false;

    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
    import * as THREE from 'three';
	import * as SC from 'svelte-cubed';
	import { onMount } from 'svelte';

    // import office from '$lib/3d/office.glb?raw';

    let spin = 0;
    let width = 0.1;
    let height = 0.1;
    let depth = 0.1;

	SC.onFrame(() => {
		spin+= 0.001;
	});

    let model;
    onMount(async () => {
        model = (await new GLTFLoader().loadAsync("https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/collision-world.glb")).scene
    })

    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, TableSearch } from 'flowbite-svelte';
    let searchTerm = '';
    let items = [
      { id: 1, ammenity: 'Toilets', number: '25', description: "Comfortable and hygienic restroom facilities strategically placed throughout the building."  },
      { id: 2, ammenity: 'Emergency Exits', number: '45', description: "Clearly marked exits designed to ensure swift and safe evacuation in case of emergencies." },
      { id: 3, ammenity: 'Prayer Rooms', number: '12', description: "Quiet and serene spaces for personal or group prayers, accommodating diverse religious needs." },
      { id: 4, ammenity: 'Pantry', number: '4', description: "Equipped kitchenette area offering refreshments and a space for light meals or snacks." }
    ];
    $: filteredItems = items.filter((item) => item.ammenity.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1);
</script>

<svelte:head>
	<title>Office</title>
	<meta name="description" content="Office Tour" />
</svelte:head>

<div class="ml-10">
    <div class="space-x-2">
        <Button class="z-10" on:click={() => {
            tourStart = false;
            panaroma = false;
        }}>
            3D render
        </Button>
        <Button class="z-10" on:click={() => {
            tourStart = false;
            panaroma = !panaroma;
        }}>
            Panaroma
        </Button>
        <Button class="z-10" on:click={() => {
            panaroma = false;
            tourStart = !tourStart;
        }}>
            Tour
        </Button>
    </div>
    
    {#if tourStart}
    <iframe class="mx-[10vw] w-[80vw] lg:mx-0 h-[70vh] mt-10" allowfullscreen title="Office Tour" style="border-style:none;" src="https://au-floor.vercel.app"></iframe>
    {:else if panaroma}
    <iframe class="mx-[10vw] w-[80vw] lg:mx-0 h-[70vh] mt-10" allowfullscreen title="Office Tour" style="border-style:none;" src="https://cdn.pannellum.org/2.4/pannellum.htm#config=https://raw.githubusercontent.com/Laikaiyong/Cpp-Labs/main/tour.json&amp;autoLoad=true"></iframe>
    {:else}
    <div class="relative mt-10 h-[70vh]">
        <SC.Canvas
            antialias
            background={new THREE.Color('papayawhip')}
            fog={new THREE.FogExp2('papayawhip', 0.1)}
            shadows
        >
            {#if model}
                <SC.Primitive object={model} scale={[width, height, depth]} rotation={[0, spin, 0]}
                />
            {:else}
            <SC.Mesh
                geometry={new THREE.BoxGeometry()}
                material={new THREE.MeshStandardMaterial({ color: 0xff3e00 })}
                scale={[width, height, depth]}
                rotation={[0, spin, 0]}
                castShadow
            />
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
    </div>
    {/if}

    <TableSearch placeholder="Search Ammenities" hoverable={true} bind:inputValue={searchTerm}>
        <TableHead>
            <TableHeadCell>ID</TableHeadCell>
            <TableHeadCell>Ammenity</TableHeadCell>
            <TableHeadCell>Number</TableHeadCell>
            <TableHeadCell>Description</TableHeadCell>
        </TableHead>
        <TableBody class="divide-y">
            {#each filteredItems as item}
            <TableBodyRow>
                <TableBodyCell>{item.id}</TableBodyCell>
                <TableBodyCell>{item.ammenity}</TableBodyCell>
                <TableBodyCell>{item.number}</TableBodyCell>
                <TableBodyCell>{item.description}</TableBodyCell>
            </TableBodyRow>
            {/each}
        </TableBody>
        </TableSearch>
</div>


<style>
</style>