 //Add an example of the 5 primary JavaScript data types to the given mapObj. 
 // The key is an example data type, and the value is the name of the data type. 
 // An object data type has already been set as the 1st key / val pair.
 const mapObj = new Map();
 mapObj.set("object",{company : "TEKsystems"});
 mapObj.set("company", "TEKsystems")
console.log(mapObj.has("company"))
 //The above console.log() statmeent returns false.
 //  Write another console.log() statement explaining why this line of code prints false.
 //  Refactor the code `mapObj.set()`, so the code : `mapObj.has() returns true.  The goal is to successfully check and see if {company : "TEKsystems"} exists in the mapObj.
 
 //loop through the mapObj and create a new array of only the data types, leaving out the example keys of the mapObj.
 //  Use array methods to do this.  Example output : ['string',number','boolean',array','object']
