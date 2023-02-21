use std::collections::HashMap;
pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut all_words = true;
    let mut note_words = HashMap::new();
    let mut mag_words = HashMap::new();
    
    for word in note.iter() {
        note_words.entry(word).and_modify(|counter| *counter += 1).or_insert(1);
    }
    for word in magazine.iter() {
        mag_words.entry(word).and_modify(|counter| *counter += 1).or_insert(1);
    }
    
    if magazine.len() < note.len() {
        all_words = false
    } else {
        for word in note.iter() {
            if !magazine.contains(&word) {
                all_words = false
            } else {
                if mag_words[&word] < note_words[&word] {
                    return false
                }
            }
        }
    }
    
    return all_words
}

fn main() {
    let magazine = "two times three is not four".split_whitespace().collect::<Vec<&str>>();
    let note = "two times two is four".split_whitespace().collect::<Vec<&str>>();
    assert!(!can_construct_note(&magazine, &note));

    let magazine = "Astronomer Amy Mainzer spent hours chatting with Leonardo DiCaprio for Netflix's 'Don't Look Up'".split_whitespace().collect::<Vec<&str>>();
    let note = "Amy Mainzer chatting with Leonardo DiCaprio"
        .split_whitespace()
        .collect::<Vec<&str>>();
    assert!(can_construct_note(&magazine, &note));
}
