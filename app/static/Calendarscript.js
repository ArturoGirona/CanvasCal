let clicked = null;
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

const days = document.getElementById('days');

const dt = new Date();
const newEventPopUp = document.getElementById('newEventPopUp');
const deleteEventPopUp = document.getElementById('deleteEventPopUp');
const eventTitleInput = document.getElementById('eventTitleInput');
const backDrop = document.getElementById('PopUpBackDrop');
const today = new Date();

//opens popup object
function openPopUp (date)
{
    clicked = date;

    const eventForDay = events.find(e => e.date === clicked);

    if (eventForDay)
    {
        document.getElementById('eventText').innerText = eventForDay.title;
        deleteEventPopUp.style.display = 'block';
        newEventPopUp.style.display ='block';
    }
    else
    {
        newEventPopUp.style.display ='block';
    }
    openPopUp.style.display = 'block';
}

function load() {
   dt.setDate(1);

   const day = dt.getDate();
   const month = dt.getMonth();
   const year = dt.getFullYear();


   const lastDay = new Date(dt.getFullYear(),
       dt.getMonth() + 1, 0).getDate();

   const prevLastDay = new Date(dt.getFullYear(),
       dt.getMonth(), 0).getDate();

   const firstDayIndex = dt.getDay();

   const lastDayIndex = new Date(dt.getFullYear(), dt.getMonth() + 1, 0).getDay();

   const nextDays = 7 - lastDayIndex - 1;

   const months = [
       "January",
       "February",
       "March",
       "April",
       "May",
       "June",
       "July",
       "August",
       "September",
       "October",
       "November",
       "December",
   ];

   document.querySelector('.date h1').innerHTML = months[dt.getMonth()];

   document.querySelector('.date p').innerHTML = new Date().toDateString();


   days.innerHTML = '';
   
   //faded out days for the prev. month
   for (let x = firstDayIndex; x > 0; x--)
   {
       const LastdayBox = document.createElement('div');
       LastdayBox.classList.add('prev-date');
       LastdayBox.innerText = (prevLastDay - x + 1);
       days.appendChild(LastdayBox);

   }

   for (let i = 1; i <= lastDay; i++)
   {
       const dayBox = document.createElement('div');
       dayBox.classList.add('day');
       dayBox.innerText = i;

       const dateString = `${month + 1}/${i}/${year}`;

       const eventForDay = events.find(e => e.date === dateString);

       //add 'event' div to day that is clicked
       if (eventForDay)
       {

           const eventDiv = document.createElement('div');
           eventDiv.classList.add('event');
           eventDiv.innerText = eventForDay.title;

           dayBox.appendChild(eventDiv);
       }


       dayBox.addEventListener('click', () => openPopUp(dateString));
       if (i === new Date().getDate() && dt.getMonth() === new Date().getMonth()){
           dayBox.id = 'today';
       }
       days.appendChild(dayBox);
       
   }
  
//the faded out days for the next month
   for(let j = 1; j <= nextDays; j++)
   {

       const NextdayBox = document.createElement('div');
       NextdayBox.classList.add('next-date')
       NextdayBox.innerText = j;
       days.appendChild(NextdayBox);
   }

}

function closePopUp()
{
    eventTitleInput.classList.remove('error');
    newEventPopUp.style.display = 'none';
    deleteEventPopUp.style.display = 'none';
    backDrop.style.display = 'none';
    eventTitleInput.value = '';
    clicked = null;
    load();
}

function saveEvent()
{
    if (eventTitleInput.value)
    {
        eventTitleInput.classList.remove('error');

        events.push({
            date: clicked,
            title: eventTitleInput.value,
        });

        localStorage.setItem('events', JSON.stringify(events));
        closePopUp();
    }
    else
    {
        eventTitleInput.classList.add('error');
    }
}

function deleteEvent()
{
    events = events.filter(e => e.date !== clicked);
    localStorage.setItem('events', JSON.stringify(events))
    closePopUp();
}



document.querySelector('.prev').addEventListener('click', () => {
   dt.setMonth(dt.getMonth() - 1);
   load();
});

document.querySelector('.next').addEventListener('click', () => {
   dt.setMonth(dt.getMonth() + 1);
   load();
});

//all the event listeners for all the buttons
document.getElementById('cancelButton').addEventListener('click', closePopUp);
document.getElementById('saveButton').addEventListener('click', saveEvent);

document.getElementById('deleteButton').addEventListener('click', deleteEvent);
document.getElementById('closeButton').addEventListener('click', closePopUp);

load();