<script>
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Tabs, TabItem } from 'flowbite-svelte';
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { Search, Button, Span, Img } from 'flowbite-svelte';
    import { SearchOutline } from 'flowbite-svelte-icons';
    import { Checkbox } from 'flowbite-svelte';
    import { Card, Listgroup, Avatar } from 'flowbite-svelte';
    import { ListgroupItem } from 'flowbite-svelte';
    import { TrashBinSolid, ArrowRightOutline } from 'flowbite-svelte-icons';
    import { AccordionItem, Accordion } from 'flowbite-svelte';

    import hlbBanner from '$lib/images/hlb-banner.jpg';


  
  </script>

<div class="font-bold dark:text-white flex flex-row ml-4 w-full">
    <span>
    <h1 class="mt-5 mb-2 text-5xl">Welcome Onboard, <Span class="font-bold text-[#00277D] dark:text-[#6696ff]">Lai Kai Yong!</Span></h1>
    <h2 class="text-xl">Hong Leong Bank welcomes you with a warm heart.</h2>
    </span>
            <Button href="/pages/1_onboard" class="ml-20 mt-10 mb-2" color="red">Continue Onboarding <ArrowRightOutline class="ml-3"/></Button>
</div>

    <Img src="/images/hlb_banner.svg" alt="hlb-banner" class="img mt-5 mb-3 ml-3" style="width: 100%;"/>

  <Tabs>
  <TabItem open title="Colleagues & Organization">
    <div class="grid grid-cols-2 gap-4">
      <div class="col-span-1" >
        <Listgroup active>
          <h3 class="p-1 text-center text-xl font-medium text-gray-900 dark:text-white">Find your colleagues</h3>
          <div class="p-3">
          <form class="flex gap-2 ">
            <Search size="md" />
            <Button class="!p-2.5" size="xs" color="red">
              <SearchOutline class="w-4 h-5" />
            </Button>
          </form>
          </div>
          
          <ListgroupItem class="text-base font-semibold gap-2">
            <Avatar src="/images/image-2@2x.jpg" size="xs" />Lee Ying Hooi
          </ListgroupItem>
          <ListgroupItem class="text-base font-semibold gap-2">
            <Avatar src="/images/image-2@2x.jpg" size="xs" />Looi Wei En
          </ListgroupItem>
          <ListgroupItem class="text-base font-semibold gap-2">
            <Avatar src="/images/image-2@2x.jpg" size="xs" />Ooi Pei Yin
          </ListgroupItem>
          <ListgroupItem class="text-base font-semibold gap-2">
            <Avatar src="/images/image-2@2x.jpg" size="xs" />Wong Jia Yi
          </ListgroupItem>
        <ListgroupItem class="text-base font-semibold gap-2">
          <Avatar src="/images/image-2@2x.jpg" size="xs" />Vandyck
        </ListgroupItem>
        </Listgroup>
      </div>
      <div class="col-span-1">
          <Listgroup active>
            <h3 class="p-1 text-center text-xl font-medium text-gray-900 dark:text-white">Organization Structure</h3>
            <!-- <form class="flex gap-2">
              <Search size="md" />
              <Button class="!p-2.5" size="xs" color="red">
                <SearchOutline class="w-4 h-5" />
              </Button>
            </form> -->
            <Accordion>
              <AccordionItem>
                <span slot="header">Board of Directors</span>
                
                <Accordion>
                  <AccordionItem>
                    <span slot="header">Chairman - Tan Wei Shen</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Tan Wei Shen</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: tan.weishen@hongleong.com </a>
                      <br>Phone: +6012-345-6789
                    </p>
                  </AccordionItem>
              
                  <AccordionItem>
                    <span slot="header">Board Member - Priya Devi</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Priya Devi</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: priya.devi@hongleong.com </a>
                      <br>Phone: +6011-987-6543
                    </p>
                  </AccordionItem>
                </Accordion>
              </AccordionItem>
            
              <AccordionItem>
                <span slot="header">Executive Management</span>
                
                <Accordion>
                  <AccordionItem>
                    <span slot="header">CEO - Ali bin Ibrahim</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Ali bin Ibrahim</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: ali.ibrahim@hongleong.com </a>
                      <br>Phone: +6019-876-5432
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">CFO - Lee Mei Ling</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Lee Mei Ling</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: lee.meiling@hongleong.com </a>
                      <br>Phone: +6013-765-4321
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">COO - Rajesh Kumar</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Rajesh Kumar</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: rajesh.kumar@hongleong.com </a>
                      <br>Phone: +6016-543-2109
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">CRO - Aishah binti Abdullah</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Aishah binti Abdullah</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: aishah.abdullah@hongleong.com </a>
                      <br>Phone: +6017-654-3210
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">CIO - Tan Ah Seng</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Tan Ah Seng</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: tan.ahseng@hongleong.com </a>
                      <br>Phone: +6014-987-0123
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">CCO - Priya Menon</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Priya Menon</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: priya.menon@hongleong.com </a>
                      <br>Phone: +6010-890-1234
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">CMO - Mohd Farid bin Hassan</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Ali bin Ibrahim</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: mohd.farid@hongleong.com </a>
                      <br>Phone: +6015-678-9012
                    </p>
                  </AccordionItem>
                </Accordion>
              </AccordionItem>
    
              <AccordionItem>
                <span slot="header">Business Unit</span>
                
                <Accordion>
                  <AccordionItem>
                    <span slot="header">Head of Retail Banking - Wong Mei Lin</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Wong Mei Lin</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: wong.meilin@hongleong.com </a>
                      <br>Phone: +6011-234-5678
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">Branch Manager - Hafizah binti Yusof</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Hafizah binti Yusof</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: hafizah.yusof@hongleong.com </a>
                      <br>Phone: +6016-789-0123
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">Relationship Manager - Arjun Singh</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Arjun Singh</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: arjun.singh@hongleong.com </a>
                      <br>Phone: Phone: +6019-012-3456
                    </p>
                  
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">Head of Commercial Banking - Nurul Huda binti Ismail</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Nurul Huda binti Ismail</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: nurul.huda.ismail@hongleong.com </a>
                      <br>Phone: +6012-345-6789
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">Investment Banker - Ganesh Kumar</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Ganesh Kumar</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: ganesh.kumar@hongleong.com </a>
                      <br>Phone: +6013-678-9012
                    </p>
                  </AccordionItem>
    
                  <AccordionItem>
                    <span slot="header">Head of Risk Management - Samantha Lee</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Samantha Lee</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: samantha.lee@hongleong.com </a>
                      <br>Phone: +6014-567-8901
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">Risk Analyst - Harith bin Rahman</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Harith bin Rahman</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: harith.rahman@hongleong.com </a>
                      <br>Phone: +6017-890-1234
                    </p>
                  </AccordionItem>
    
                  <AccordionItem>
                    <span slot="header">Head of Compliance - Ravi Shankar</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center"> Ravi Shankar</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: ravi.shankar@hongleong.com </a>
                      <br>Phone: +6018-901-2345
                    </p>
                  </AccordionItem>
                
                  <AccordionItem>
                    <span slot="header">Compliance Officer - Nurul Izzati binti Jamal</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Nurul Izzati binti Jamal</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: nurul.izzati.jamal@hongleong.com </a>
                      <br>Phone: +6019-123-4567
                    </p>
                  </AccordionItem>
                </Accordion>
              </AccordionItem>
    
              <AccordionItem>
                <span slot="header">Support Functions</span>
                
                <Accordion>
                  <AccordionItem>
                    <span slot="header">CFO - Lim Chee Keong</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Lim Chee Keong</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: lim.cheekeong@hongleong.com </a>
                      <br>Phone: +6010-234-5678
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">Internal Auditor - Saraswathi Devi</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Saraswathi Devi</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: saraswathi.devi@hongleong.com </a>
                      <br>Phone: +6011-345-6789
                    </p>
                  </AccordionItem>
    
                  <AccordionItem>
                    <span slot="header">Treasury Manager - Ng Kim Choo</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Ng Kim Choo</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: ng.kimchoo@hongleong.com </a>
                      <br>Phone: +6012-456-7890
                    </p>
                  </AccordionItem>
                </Accordion>
              </AccordionItem>
    
              <AccordionItem>
                <span slot="header">Retail Banking Branches</span>
                
                <Accordion>
                  <AccordionItem>
                    <span slot="header">Branch Manager - Ahmad bin Hassan</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Ahmad bin Hassan</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: ahmad.hassan@hongleong.com </a>
                      <br>Phone: +6013-567-8901
                    </p>
                  
                  </AccordionItem>
                  
                  <AccordionItem>
                    <span slot="header">Assistant Branch Manager - Lim Mei Ling</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Lim Mei Ling</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: lim.meiling@hongleong.com </a>
                      <br>Phone: +6014-678-9012
                    </p>
                  </AccordionItem>
    
                  <AccordionItem>
                    <span slot="header">Customer Service Representative - Farah binti Abdul Razak</span>
                    <Img src="/images/image-2@2x.jpg" alignment="mx-auto"size="md" class="rounded-lg"/>
                    <p class="mb-2 text-gray-900 dark:text-gray-400 ml-auto center">Farah binti Abdul Razak</p>
                    <p class="text-gray-500 dark:text-gray-400">
                      <a href= mailto: > Email: farah.abdulrazak@hongleong.com </a>
                      <br>Phone: +6015-789-0123
                    </p>
                  </AccordionItem>
                </Accordion>
              </AccordionItem>
    
            </Accordion>
          </Listgroup>
        </div>
    </div>

  </TabItem>
  
  <TabItem title="Tasks List">
      <ul class="bg-white rounded-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-600 divide-y divide-gray-200 dark:divide-gray-600">
        <li> <h3 class="p-1 text-center text-xl font-medium text-gray-900 dark:text-white">Task list</h3></li>
        
        <li><Checkbox class="p-3">Networking Session      
          <div class="category ml-auto"><Button size="xs" outline color="red" pill>Category</Button></div>
          <div class="date ml-auto"> 25 Nov 2023 </div></Checkbox> </li>
        <li><Checkbox class="p-3">Understand Company Policies 
          <div class="category ml-auto"><Button size="xs" outline color="red" pill>Category</Button></div>
          <div class="date ml-auto"> 25 Nov 2023 </div></Checkbox></li>
        <li><Checkbox class="p-3">Company Tour 
          <div class="category ml-auto"><Button size="xs" outline color="red" pill>Category</Button></div>
          <div class="date ml-auto"> 25 Nov 2023 </div></Checkbox></li>
        <li><Checkbox class="p-3">Set Up Professional Profiles
          <div class="category ml-auto"><Button size="xs" outline color="red" pill>Category</Button></div>
          <div class="date ml-auto"> 25 Nov 2023 </div></Checkbox></li>
        
      </ul>
  </TabItem>
  </Tabs>

  