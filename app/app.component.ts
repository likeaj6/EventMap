import { Component, OnInit} from '@angular/core';

import { Event } from './event';
import { EventService } from './event.service';

//declare var google: any;

@Component({
  selector: 'my-app',
  template: `
      <h1>{{title}}</h1>
      <div id="googleMap"></div>
      <my-events></my-events>
  `,
  providers: [EventService]
})

export class AppComponent implements OnInit {
  title = 'Swat Events Map';
  constructor(private eventService: EventService) {}

  getEvents(): void {
    this.eventService.getEvents().then(events => this.events = events);
  }

  createMarker(Event e): void {
    var marker = new google.maps.Marker({
      position: {lat: e.lat, lng: e.lng},
      map: map,
      label: e.name
    });
  }
  ngOnChanges(): void {
    this.getEvents();
  }
  ngOnInit(): void {
    var mapProp = {
      center: new google.maps.LatLng(39.905271, -75.354344),
      zoom: 17,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    var event1 = new Event({id: 0, name: "MLH Local Hack Day", start_time:"9:00AM", end_time:"9:00PM", location: "sci center", lat:39.905271, lng:-75.354344, description:" "});
    //createMarker(event1);
    // var marker = new google.maps.Marker({
    //   position: {lat: event1.lat, lng: event1.lng},
    //   map: map,
    //   label: event1.name
    // });
    //this.events.forEach(createMarker(e))
  }
  //convertEventIntoLocation(lat, lng): var {
    //return {lat: lat, lng: lng};
  //}
}
