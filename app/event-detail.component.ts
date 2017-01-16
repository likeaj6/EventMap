import { Component, Input } from '@angular/core';

import { Event } from './event';

@Component({
  selector: 'my-event-detail',
  template: `
    <div id="eventDetails"*ngIf="event">
      <h2>{{event.name}} details:</h2>
      <h4><div>
        <label>name: </label>
        <input [(ngModel)]="event.name" placeholder="name"/>
      </div></h4>
      <h4><div>
        <label>location: </label>
        {{event.location}}
      </div></h4>
      <h4><div>
        <label>start time: </label>
        {{event.start_time}}
      </div></h4>
      <h4><div>
        <label>end time: </label>
        {{event.end_time}}
      </div></h4>
      <h4><div>
        <label>description: </label>
        {{event.description}}
      </div></h4>
    </div>
  `,

})
export class EventDetailComponent {
  @Input()
  event: Event;
}
