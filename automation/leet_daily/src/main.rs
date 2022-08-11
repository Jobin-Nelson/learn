use std::collections::HashMap;
use std::path::{Path, PathBuf};
use std::fs;
use std::io::prelude::*;
use serde_json::Value;
use reqwest::Error;

fn main() -> Result<(), Error>{
    let mut map = HashMap::new();
    map.insert("query", "query questionOfToday {\n\tactiveDailyCodingChallengeQuestion {\n\t\tdate\n\t\tlink\n\t}\n}\n");
    map.insert("operationName", "questionOfToday");

    let base_url = "https://leetcode.com/";
    let client = reqwest::blocking::Client::new();

    let response = client.post(format!("{}graphql/", base_url))
        .json(&map)
        .send()?
        .text()?;
    
    let data: Value = serde_json::from_str(&response).expect("Could not deserialize the response");

    let date = &data["data"]["activeDailyCodingChallengeQuestion"]["date"].as_str().unwrap();
    let link = &data["data"]["activeDailyCodingChallengeQuestion"]["link"].as_str().unwrap();
    let file_name = Path::new(&link).file_name().unwrap();
    let month = chrono::Utc::now().format("%B").to_string().to_ascii_lowercase();
    let mut file_path: PathBuf = PathBuf::from("/home/jobin/playground/learn/competitive_programming");
    file_path.push(month);

    fs::create_dir_all(file_path.as_path()).expect("Couldn't create directory");

    file_path.push(file_name);
    file_path.set_extension("py");

    if !file_path.exists() {

        let content = format!("\
'''
Created Date: {}
Qn:
Link: {}
Notes:
'''
def main():
    pass
    
if __name__ == '__main__':
",
            date, link);

        let mut f = fs::File::create(&file_path).unwrap();
        let _ = f.write_all(content.as_bytes()).unwrap();

    };
    
    Ok(())
}
