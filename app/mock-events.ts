import { Event } from './event';
var data;
var array = [];
var ref = firebase.database().ref('events')
}
ref.on('value',function(snap){
    snap.forEach(function(childSnapshot){
        var key = childSnapshot;
        //var data = childSnapshot.val();
        data = childSnapshot.val();
        array.push({
          name: data.name,
          start_time: data.start_time,
          end_time: data.end_time,
          location: data.location,
          lat: data.lat,
          lng: data.lng,
          description: data.description
        });
        //console.log(dict)
        //array.push(dict.toString());
    //data = snap.exportVal();
   });
console.log(JSON.stringify(array))

export const EVENTS: Event[] = JSON.stringify(array);
