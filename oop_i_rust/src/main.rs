use std::str::FromStr;
#[macro_use]
extern crate fstrings;

struct Date {
    day: i32,
    month: i32,
    year: i32,
}

impl Date {
    pub fn get_date_from_string(date: String) -> Date {
        let split_date = date.split("-").collect::<Vec<&str>>();
        let day = FromStr::from_str(split_date[0 as usize]).unwrap();
        let month = FromStr::from_str(split_date[1 as usize]).unwrap();
        let year = FromStr::from_str(split_date[2 as usize]).unwrap();
        Date{day:day, month:month, year:year}
    }
    pub fn set_date_from_string(&mut self, date: String) {
        let split_date = date.split("-").collect::<Vec<&str>>();
        self.day = FromStr::from_str(split_date[0 as usize]).unwrap();
        self.month = FromStr::from_str(split_date[1 as usize]).unwrap();
        self.year = FromStr::from_str(split_date[2 as usize]).unwrap();
    }
    pub fn date_as_string(&self) -> String {
        let day: String = self.day.to_string();
        let week: String = self.month.to_string();
        let year: String = self.year.to_string();
        String::from(f!("{day}-{week}-{year}"))
    }
}

struct Package {
    resipiant_address: String,
    sender_address: String,
    price: i32,
    send_date: Date
}


fn main() {
    let mut dato = Date::get_date_from_string(String::from("05-02-2003"));
    dato.set_date_from_string(String::from("20-04-2004"));
    let dato_string = dato.date_as_string();
    println!("{}", dato_string);
}
