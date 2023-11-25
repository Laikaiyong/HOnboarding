<script>
    import { createEventDispatcher } from 'svelte';
  
    /** @type {string[]} */
    export let headers = [];
  
    /** @type {{ name: string; enabled: boolean; date: Date; }[]} */
    export let days = [];
  
    /**
     * @typedef {Object} CalendarItem
     * @property {string} title
     * @property {Date} date
     * @property {string} className
     * @property {number} len
     * @property {boolean | undefined} isBottom
     * @property {string | undefined} detailHeader
     * @property {string | undefined} detailContent
     * @property {number | undefined} vlen
     * @property {number | undefined} startCol
     * @property {number | undefined} startRow
     */
  
    /** @type {CalendarItem[]} */
    export let items = [];
  
    let dispatch = createEventDispatcher();
  </script>
  
  <div class="calendar">
    {#each headers as header}
      <div
        role="button"
        tabindex="0"
        class="day-name"
        on:click={() => dispatch('headerClick', header)}
        on:keydown={(e) => e.key === 'Enter' && dispatch('headerClick', header)}
      >
        {header}
      </div>
    {/each}
  
    {#each days as day}
      {#if day.enabled}
        <div
          role="button"
          tabindex="0"
          class="day"
          on:click={() => dispatch('dayClick', day)}
          on:keydown={(e) => e.key === 'Enter' && dispatch('dayClick', day)}
        >
          {day.name}
        </div>
      {:else}
        <div
          role="button"
          tabindex="0"
          class="day day-disabled"
          on:click={() => dispatch('dayClick', day)}
          on:keydown={(e) => e.key === 'Enter' && dispatch('dayClick', day)}
        >
          {day.name}
        </div>
      {/if}
    {/each}
  
    {#each items as item}
      <section
        role="button"
        tabindex="0"
        on:click={() => dispatch('itemClick', item)}
        on:keydown={(e) => e.key === 'Enter' && dispatch('itemClick', item)}
        class="task {item.className}"
        style="grid-column: {item.startCol} / span {item.len};
               grid-row: {item.startRow};
               align-self: {item.isBottom ? 'end' : 'center'};"
      >
        {item.title}
        {#if item.detailHeader}
          <div class="task-detail">
            <h2>{item.detailHeader}</h2>
            <p>{item.detailContent}</p>
          </div>
        {/if}
      </section>
    {/each}
  </div>
  
  <style>
    .calendar {
      display: grid;
      width: 100%;
      grid-template-columns: repeat(7, minmax(120px, 1fr));
      grid-template-rows: 50px;
      grid-auto-rows: 120px;
      overflow: auto;
    }
  
    .day {
      /* ... existing styles ... */
    }
  
    .day-name {
      font-size: 12px;
      text-transform: uppercase;
      color: #e9a1a7;
      text-align: center;
      border-bottom: 1px solid rgba(166, 168, 179, 0.12);
      line-height: 50px;
      font-weight: 500;
      cursor: pointer;
    }
  
    .day-disabled {
      /* ... existing styles ... */
    }
  
    .task {
      /* ... existing styles ... */
    }
  
    .task-detail {
      /* ... existing styles ... */
    }
  </style>