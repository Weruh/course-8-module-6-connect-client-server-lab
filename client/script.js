const API_URL = "http://localhost:5000/events";

const form = document.querySelector("form");
const titleInput = document.querySelector("#title");
const eventList = document.querySelector("#event-list");

fetch(API_URL)
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })
  .catch(error => console.error("Failed to load events:", error));

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = titleInput.value.trim();

  if (!title) {
    alert("Please enter an event title.");
    return;
  }

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.error); });
      }
      return response.json();
    })
    .then(newEvent => {
      renderEvent(newEvent);
      form.reset();
    })
    .catch(error => alert(`Could not add event: ${error.message}`));
});

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  eventList.appendChild(li);
}
