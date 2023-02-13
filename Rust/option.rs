pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        if self.health == 0 && self.level <= 9 {
            Some(Player {health: 100, mana: None, level: self.level})
        } else if self.health == 0 && self.level > 9{
            Some(Player {health: 100, mana: Some(100), level: self.level})
        } else {
            None
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if self.level < 10 {
            if self.health >= mana_cost {
                self.health -= mana_cost;
            } else {
                self.health = 0;
            }
            return 0
        } else if self.mana.unwrap() < mana_cost {
            return 0
        } else {
            self.mana = Some(self.mana.unwrap() - mana_cost);
            return mana_cost * 2
        }
    }

    pub fn health(&self) -> u32 {
        return self.health;
    }

    pub fn mana(&self) -> Option<u32> {
        return self.mana;
    }

    pub fn level(&self) -> u32 {
        return self.level;
    }
}

fn main(){
    let dead_player = Player { health: 0, mana: None, level: 2};
    let mut player1 = Player { health: 100, mana:None, level: 5};
    
    println!("Dead player: ");
    print!("\t Health: {:?} \t", dead_player.health);
    print!("\t Mana: {:?} \t", dead_player.mana);
    println!("\t Level: {:?} \t", dead_player.level);

    println!("Player 1: ");
    print!("\t Health: {:?} \t", player1.health);
    print!("\t Mana: {:?} \t", player1.mana);
    println!("\t Level: {:?} \t", player1.level);

    player1.cast_spell(20);
    println!("Player 1 after attempted spell: ");
    print!("\t Health: {:?} \t", player1.health);
    print!("\t Mana: {:?} \t", player1.mana);
    println!("\t Level: {:?} \t", player1.level);
}
