<script>
    import Calendar from "./Calendar.svelte";
    import {onMount} from 'svelte';
  
    var dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    let monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  
    /**
     * @type {string[]}
     */
    let headers = [];
  
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
  
    /**
     * @type {CalendarItem[]}
     */
    var items = [];
  
    /**
     * @type {{ name: string; enabled: boolean; date: Date }[]}
     */
    let days = [];
  
    let now = new Date();
    let year = now.getFullYear();
    let month = now.getMonth();
    let eventText = "Click an item or date";
  
    function initMonthItems() {
      let y = year;
      let m = month;
      let d1 = new Date(y, m, randInt(7) + 7);
      
      /**
 * @type {CalendarItem[]}
 */
var items = [
  { title: "11:00 Task Early in month", className: "task--primary", date: new Date(y, m, randInt(6)), len: randInt(4) + 1, isBottom: false, detailHeader: "", detailContent: "", vlen: 0, startCol: 0, startRow: 0 },
  { title: "7:30 Wk 2 tasks", className: "task--warning", date: d1, len: randInt(4) + 2, isBottom: false, detailHeader: "", detailContent: "", vlen: 0, startCol: 0, startRow: 0 },
  { title: "Overlapping Stuff (isBottom:true)", date: d1, className: "task--info", len: 4, isBottom: true, detailHeader: "", detailContent: "", vlen: 0, startCol: 0, startRow: 0 },
  { title: "10:00 More Stuff to do", date: new Date(y, m, randInt(7) + 14), className: "task--info", len: randInt(4) + 1, isBottom: false, detailHeader: "Difficult", detailContent: "But not especially so", vlen: 0, startCol: 0, startRow: 0 },
  { title: "All day task", date: new Date(y, m, randInt(7) + 21), className: "task--danger", len: 1, vlen: 2, isBottom: false, detailHeader: "", detailContent: "", startCol: 0, startRow: 0 },
];

  
      for (let i of items) {
        let rc = findRowCol(i.date);
        if (rc == null) {
          console.log('didn`t find date for ', i);
          console.log(i.date);
          console.log(days);
          i.startCol = i.startRow = 0;
        } else {
          i.startCol = rc.col;
          i.startRow = rc.row;
        }
      }
    }
  
    $: month, year, initContent();
  
    function initContent() {
      headers = dayNames;
      initMonth();
      initMonthItems();
    }
  
    function initMonth() {
      days = [];
      let monthAbbrev = monthNames[month].slice(0, 3);
      let nextMonthAbbrev = monthNames[(month + 1) % 12].slice(0, 3);
      var firstDay = new Date(year, month, 1).getDay();
      var daysInThisMonth = new Date(year, month + 1, 0).getDate();
      var daysInLastMonth = new Date(year, month, 0).getDate();
      var prevMonth = month == 0 ? 11 : month - 1;
  
      for (let i = daysInLastMonth - firstDay; i < daysInLastMonth; i++) {
        let d = new Date(prevMonth == 11 ? year - 1 : year, prevMonth, i + 1);
        days.push({ name: '' + (i + 1), enabled: false, date: d, });
      }
  
      for (let i = 0; i < daysInThisMonth; i++) {
        let d = new Date(year, month, i + 1);
        if (i == 0) days.push({ name: monthAbbrev + ' ' + (i + 1), enabled: true, date: d, });
        else days.push({ name: '' + (i + 1), enabled: true, date: d, });
      }
  
      for (let i = 0; days.length % 7; i++) {
        let d = new Date((month == 11 ? year + 1 : year), (month + 1) % 12, i + 1);
        if (i == 0) days.push({ name: nextMonthAbbrev + ' ' + (i + 1), enabled: false, date: d, });
        else days.push({ name: '' + (i + 1), enabled: false, date: d, });
      }
    }
  
/**
 * @param {Date} dt
 */

    function findRowCol(dt) {
      for (let i = 0; i < days.length; i++) {
        let d = days[i].date;
        if (d.getFullYear() === dt.getFullYear() && d.getMonth() === dt.getMonth() && d.getDate() === dt.getDate())
          return { row: Math.floor(i / 7) + 2, col: i % 7 + 1 };
      }
      return null;
    }
  
/**
 * @param {{ date: Date }} e
 */    

    function itemClick(e) {
      eventText = 'itemClick ' + JSON.stringify(e) + ' localtime=' + e.date.toString();
    }
  
/**
 * @param {{ date: Date }} e
 */

    function dayClick(e) {
      eventText = 'onDayClick ' + JSON.stringify(e) + ' localTime=' + e.date.toString();
    }
  

/**
 * @param {{ date: Date }} e
 */

    function headerClick(e) {
      eventText = 'onHheaderClick ' + JSON.stringify(e);
    }
  
    function next() {
      month++;
      if (month == 12) {
        year++;
        month = 0;
      }
    }
  
    function prev() {
      if (month == 0) {
        month = 11;
        year--;
      } else {
        month--;
      }
    }
  
/**
 * @param {number} max
 */

    function randInt(max) {
      return Math.floor(Math.random() * max) + 1;
    }
  
    onMount(() => {
      initContent();
    });
  </script>
  
  <div class="calendar-container">
    <div class="calendar-header">
      <h1>
        <button on:click={() => year--}>&Lt;</button>
        <button on:click={() => prev()}>&lt;</button>
        {monthNames[month]} {year}
        <button on:click={() => next()}>&gt;</button>
        <button on:click={() => year++}>&Gt;</button>
      </h1>
      {eventText}
    </div>
  
    <Calendar
      headers={headers}
      days={days}
      items={items}
      on:dayClick={(e) => dayClick(e.detail)}
      on:itemClick={(e) => itemClick(e.detail)}
      on:headerClick={(e) => headerClick(e.detail)}
    />
  </div>
  
  <style>
    .calendar-container {
      width: 90%;
      margin: auto;
      overflow: hidden;
      box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
      border-radius: 10px;
      background: #fff;
      max-width: 1200px;
    }
  
    .calendar-header {
      text-align: center;
      padding: 20px 0;
      background: #eef;
      border-bottom: 1px solid rgba(166, 168, 179, 0.12);
    }
  
    .calendar-header h1 {
      margin: 0;
      font-size: 18px;
    }
  
    .calendar-header button {
      background: #eef;
      border: 1px;
      padding: 6;
      color: rgba(81, 86, 93, 0.7);
      cursor: pointer;
      outline: 0;
    }
  </style>
  