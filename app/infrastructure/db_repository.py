from domain.skill import Skill
from typing import List
import psycopg2

# This is the interface for using the SQLite repository
class PostgreSQLRepository:
    # Create the database
    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.create_skill_table()

    def create_skill_table(self) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS skills (
                user_id INTEGER NULL,
                skill_name TEXT NOT NULL,
                count INTEGER NOT NULL,
                PRIMARY KEY (skill_name)
            )
        ''')
        conn.commit()
        conn.close()

    def add_skill(self, skill: Skill) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            INSERT INTO skills (skill_name, count) VALUES (?, ?)
        ''', (skill.get_name(), skill.get_count(),))
        conn.commit()
        conn.close()
    
    def get_all_skills(self) -> List[Skill]:    
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            SELECT skill_name, count FROM skills
        ''')
        skills = [Skill(row[0], row[1]) for row in c.fetchall()]
        conn.commit()
        conn.close()
        return skills

    def remove_skill(self, skill: Skill) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            DELETE FROM skills WHERE skill_name = ?
        ''', (skill.get_name(),))
        conn.commit()
        conn.close()

    def decrement_skill(self, skill: Skill) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            UPDATE skills SET count = count - 1 WHERE skill_name = ?
        ''', (skill.get_name(),))
        conn.commit()
        conn.close()

    def increment_skill(self, skill: Skill) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            UPDATE skills SET count = count + 1 WHERE skill_name = ?
        ''', (skill.get_name(),))
        conn.commit()
        conn.close()

    def get_skill(self, skill_name: str) -> Skill:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            SELECT skill_name, count FROM skills WHERE skill_name = ?
        ''', (skill_name,))
        skill = Skill(row[0], row[1]) if (row := c.fetchone()) else None
        conn.close()
        return skill

 
    def drop_skill_table(self) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            DROP TABLE IF EXISTS skills
        ''')
        conn.commit()
        conn.close()
    
    def drop_database(self) -> None:
        conn = psycopg2.connect(self.db_url)
        c = conn.cursor()
        c.execute('''
            DROP DATABASE IF EXISTS skills_database
        ''')
        conn.commit()
        conn.close()
    
    def close_connection(self) -> None:
        conn = psycopg2.connect(self.db_url)
        conn.close()
