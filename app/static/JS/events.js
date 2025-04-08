document.addEventListener('DOMContentLoaded', () => {

    const eventsContainer = document.getElementById('events-container');
    const eventCardTemplate = document.getElementById('event-card-template');
    const modal = document.getElementById('eventModal');
    const eventDetailContent = document.getElementById('eventDetailContent');
    const closeBtn = document.querySelector('.modal-close');

    let currentFilter = 'all';
    let eventsData = [];

    async function loadEvents() {
        try {
            const response = await fetch('/api/events');
            eventsData = await response.json();
            console.log('Données reçues:', eventsData);
            renderEvents(eventsData);
        } catch (error) {
            console.error('error while loading event:', error);
            eventsContainer.innerHTML = `<div class="error"> An error occurred while loading event details.</div>`;
        }
    }

    function renderEvents(events) {
        eventsContainer.innerHTML = '';

        
        if (!Array.isArray(events)) {
            console.error('error:', events);
            eventsContainer.innerHTML = `<div class="error">Incorrect format.</div>`;
            return;
        }

        let filteredEvents = events;
        if (currentFilter !== 'all') {
            filteredEvents = events.filter(event => event.status === currentFilter);
        }

        if (filteredEvents.length === 0) {
            eventsContainer.innerHTML = `<div class="no-events">No event</div>`;
            return;
        }

        filteredEvents.forEach(event => {
            const eventCard = createEventCard(event);
            eventsContainer.appendChild(eventCard);
        });
    }

    function createEventCard(event) {
        const template = eventCardTemplate.content.cloneNode(true);

        const card = template.querySelector('.event-card');
        card.setAttribute('data-id', event.id);
        card.setAttribute('data-category', event.status);

        const image = template.querySelector('.event-image');
        image.src = event.image_url;
        image.alt = event.title;

        template.querySelector('.event-category').textContent = event.category;
        template.querySelector('.event-title').textContent = event.title;
        template.querySelector('.event-date').textContent = event.date;
        template.querySelector('.event-time').textContent = event.time;
        template.querySelector('.event-location').textContent = event.location;
        template.querySelector('.event-description').textContent = event.short_description;

        const detailsBtn = template.querySelector('.event-details-btn');
        detailsBtn.addEventListener('click', (e) => {
            e.preventDefault();
            openEventDetails(event.id);
        });

        return template;
    }

    async function openEventDetails(eventId) {
        try {
            const response = await fetch(`/api/events/${eventId}`);
            const eventData = await response.json();

            console.log('eventData:', eventData);

            renderEventDetails(eventData);

            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';

        } catch (error) {
            console.error('error while loading the events', error);
            eventDetailContent.innerHTML = `<div class="error">An error occurred while loading event details.</div>`;
        }
    }

    function renderEventDetails(event) {
        
        eventDetailContent.innerHTML = ``;

        // Ajouter les écouteurs d'événements aux onglets
        const tabs = eventDetailContent.querySelectorAll('.tab');
        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Retirer la classe active de tous les onglets
                tabs.forEach(t => t.classList.remove('active'));

                // Ajouter la classe active à l'onglet cliqué
                tab.classList.add('active');

                // Retirer la classe active de tous les contenus d'onglet
                const tabContents = eventDetailContent.querySelectorAll('.tab-content');
                tabContents.forEach(content => content.classList.remove('active'));

                // Ajouter la classe active au contenu d'onglet correspondant
                const tabId = tab.getAttribute('data-tab');
                const tabContent = eventDetailContent.querySelector(`#${tabId}`);
                if (tabContent) {
                    tabContent.classList.add('active');
                }
            });
        });
    }

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    
    document.querySelectorAll('.event-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.event-tab').forEach(t => {
                t.classList.remove('active');
            });

            tab.classList.add('active');

            currentFilter = tab.getAttribute('data-tab');
            renderEvents(eventsData);
        });
    });

    
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Chargement initial des événements
    loadEvents();
});