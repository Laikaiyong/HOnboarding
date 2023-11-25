<script>
    import {
      Button, Checkbox, Tabs, TabItem, Modal, 
    } from 'flowbite-svelte';

    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
    import * as THREE from 'three';
    import * as SC from 'svelte-cubed';
    import { onMount } from 'svelte';
    import { Dropdown, DropdownItem, Radio, Helper } from 'flowbite-svelte';
    import { ChevronDownSolid, ChevronRightSolid } from 'flowbite-svelte-icons';
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, TableSearch } from 'flowbite-svelte';

    // import office from '$lib/3d/office.glb?raw';

    import { apiData, drinkNames } from './onboard.js';

   

    let width = 0.76;
    let height = 0.76;
    let depth = 0.76;
    let group = 2;

    let model;
    onMount(async () => {
        model = (await new GLTFLoader().loadAsync("https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/Michelle.glb")).scene
    })

    let defaultModal=false;
</script>

<svelte:head>
	<title>Onboard</title>
	<meta name="description" content="Onboard" />
</svelte:head>

<div class="my-1">
    <h2 class='text-4xl font-bold pt-1 pb-0 dark:text-white'>E-Sensei</h2> 
    <div class="dropdown">
        <Button color="red">Select Onboarding Type<ChevronDownSolid class="w-3 h-3 ml-2 text-white dark:text-white" /></Button>
        <Dropdown class="w-60 p-3 space-y-1">
            <DropdownItem>General</DropdownItem>
            
          <DropdownItem class="flex items-center justify-between">
            Department Specific
            <ChevronRightSolid class="w-3 h-3 ml-2 text-primary-700 dark:text-white" />
          </DropdownItem>
          <Dropdown placement="right-start">
            <DropdownItem>Marketing & Communication</DropdownItem>
            <DropdownItem>Human Resources</DropdownItem>
            <DropdownItem>IT Application Support</DropdownItem>
            <DropdownItem>Operations & Customer Service</DropdownItem>
          </Dropdown>
        
          <DropdownItem>New Employee Onboarding</DropdownItem>
          <DropdownItem class="flex items-center justify-between">Training and Development
            <ChevronRightSolid class="w-3 h-3 ml-2 text-primary-700 dark:text-white" />
          </DropdownItem>
          <Dropdown placement="right-start">
            <DropdownItem>Financial Products and Services</DropdownItem>
            <DropdownItem>Cybersecurity Awareness</DropdownItem>
            <DropdownItem>Sales Techniques</DropdownItem>
            <DropdownItem>Leadership Development</DropdownItem>
          </Dropdown>
          <!-- <DropdownItem slot="footer">Sign out</DropdownItem> -->
        </Dropdown>
    </div>

    <div class='flex flex-row mt-2'>
        <div class='basis-1/2'>    
            <iframe title="Bedrock" src="http://localhost:8501/?nav=digitalhuman" class="w-[40vw] h-[80vh]" frameborder="0"></iframe>
        </div>
        
        <div class='basis-1/2'>
        <Tabs>
            <TabItem open title="Digital Human">
                <div class="relative h-[60vh]">
                    <SC.Canvas
                        antialias
                        background={new THREE.Color('papayawhip')}
                        fog={new THREE.FogExp2('papayawhip', 0.1)}
                        shadows
                    >
                        {#if model}
                            <SC.Primitive object={model} scale={[width, height, depth]}
                            />
                        {:else}
                        <SC.Mesh
                            geometry={new THREE.BoxGeometry()}
                            material={new THREE.MeshStandardMaterial({ color: 0xff3e00 })}
                            scale={[width, height, depth]}
                            castShadow
                        />
                        {/if}
                        <SC.PerspectiveCamera position={[0, 2, 5]} zoom={1.5} />
                        <SC.OrbitControls enableZoom={true} maxPolarAngle={Math.PI * 0.51} />
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
            </TabItem>
            <TabItem title="Mortal">
              <iframe class="w-full h-[60vh]" src="https://app.heygen.com/embeds/b1494bf796bf4e13908c154ee161f0ad" title="HeyGen video player" frameborder="0" allow="encrypted-media; fullscreen;" allowfullscreen></iframe>
            </TabItem>
            <TabItem title="Onboarding Progress"> 
                <Table hoverable={true} class="p-2">
                    <TableHead>
                      <TableHeadCell class="!p-4">
                      </TableHeadCell>
                      <TableHeadCell>Session Type</TableHeadCell>
                      <TableHeadCell>Progress</TableHeadCell>
                      <TableHeadCell>Status</TableHeadCell>
                    </TableHead>
            
                    <TableBody class="divide-y">
            
                      <TableBodyRow>
                        <TableBodyCell class="!p-4">
                        </TableBodyCell>
                        <TableBodyCell>Orientation</TableBodyCell>
                        <TableBodyCell>2/2</TableBodyCell>
                        <TableBodyCell><span class="font-bold text-[#05b802] dark:text-[#05b802]">Done</span></TableBodyCell>
                      </TableBodyRow>
            
            
                      <TableBodyRow>
                        <TableBodyCell class="!p-4">
                        </TableBodyCell>
                        <TableBodyCell on:click={() => (defaultModal = true)}>Training</TableBodyCell>
                        <TableBodyCell>8/19</TableBodyCell>
                        <TableBodyCell><span class="font-bold text-[#e8be00] dark:text-[#e8be00]">In progress</span></TableBodyCell>
                        <Modal title="Training Categories" bind:open={defaultModal} autoclose>
                          <div class="grid grid-cols-2 gap-4">
                            <div class="col-span-1">
                              <p class="text-base leading-relaxed font-bold text-gray-500 dark:text-gray-400">Text-based Training</p>
                              <p class="text-gray-500 dark:text-gray-400"></p>
                              <Button href="/chat">Text</Button>
                            </div>
                            <div class="col-span-1">
                              <p class="text-base leading-relaxed font-bold text-gray-500 dark:text-gray-400">Audio-based Training</p>
                              <Button href="/audio">Audio</Button>
                            </div>
                          </div>
                          <svelte:fragment slot="footer">
                            <Button class="items-end" color="alternative">Back</Button>
                          </svelte:fragment>
                        </Modal>
                      </TableBodyRow>
            
            
                      <TableBodyRow>
                        <TableBodyCell class="!p-4">
                        </TableBodyCell>
                        <TableBodyCell>Video</TableBodyCell>
                        <TableBodyCell>5/29</TableBodyCell>
                        <TableBodyCell><span class="font-bold text-[#e8be00] dark:text-[#e8be00]">In progress</span></TableBodyCell>
                      </TableBodyRow>
            
                      <TableBodyRow>
                        <TableBodyCell class="!p-4">
                        </TableBodyCell>
                        <TableBodyCell>Assessment</TableBodyCell>
                        <TableBodyCell>0/3</TableBodyCell>
                        <TableBodyCell><span class="font-bold text-[#f54542] dark:text-[#f54542]">Pending</span></TableBodyCell>
                      </TableBodyRow>
            
                    </TableBody>
                  </Table>
            </TabItem>
        </Tabs>
    </div>
    </div>
</div>






<style>

    .dropdown{
        padding: 10px;
        margin-left: 0px;
    }
    .table{
        padding: 0px;
        float: right;
        margin-right: 90px;
    }
    
</style>