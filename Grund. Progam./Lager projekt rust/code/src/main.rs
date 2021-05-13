// Imports 
    use std::io::{self};
//

#[derive(Clone)]
struct Location {
    address: String,
    city: String,
    zip: i32,
}

struct Item {
    name: String,
    location: Location
}

impl Item {
    //pub fn get_location(&self) -> &Location { &self.location }
    pub fn get_address(&self) -> String { self.location.address.clone() }
}

struct Items {
    items: Vec<Item>
}

impl Items {
    pub fn get_items(&mut self) -> &mut Vec<Item> { &mut self.items }
    pub fn get_item(&mut self, indent: usize) -> &Item { &mut self.items[indent] }
    pub fn add_item(&mut self, item: Item) { self.items.push(item); }
}

fn tests() {
    let location = Location{ address:String::from("Agri college"), city:String::from("Aalborg"), zip:9000 };
    let item = Item{ name:String::new(), location:location.clone() };
    assert_eq!(location.address.clone(), item.get_address());
    assert_ne!(String::from("Tech college"), item.get_address());
}

fn main(){

    // Tester structs
    tests();

    // Definere MENU variable, holder en vector med linjer der skal printes for at vise menu'en
    let MENU: Vec<String> = vec![
        String::from("#############################"),
        String::from("# 1. New item               #"),
        String::from("# 2. New address            #"),
        String::from("# 3. Print item             #"),
        String::from("# 4. Print items at address #"),
        String::from("#############################"),
        ];
    // Laver en Items instans som holder instanser af Item

    // Printer menu'en
    for i in MENU {
        println!("{}",i);
    }

    // Tager input
    print!("Select one:");
    let mut buffer = String::new();
    let stdin = io::stdin(); // We get `Stdin` here.
    match stdin.read_line(&mut buffer) {
        Ok(_) => {},
        Err(_) => {},
    }
    match &buffer[..] {
        "1" => {}
        "2" => {}
        "3" => {}
        "4" => {}
        &_ => {}
    }
}