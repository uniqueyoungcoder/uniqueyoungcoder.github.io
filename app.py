from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary of stories with summaries
stories = {
    "The Three Little Pigs": {
        "author": "Unknown, 2012 adaptation",
        "year": 2012,
        "summary": "Three pigs build houses of straw, sticks, and bricks to protect themselves from a cunning wolf. The wolf blows down the first two houses but fails against the sturdy brick house. The pigs outsmart the wolf, who falls into a pot of boiling water, ensuring their safety."
    },
    "The Ugly Duckling": {
        "author": "Hans Christian Andersen",
        "year": 1843,
        "summary": "A duckling, mocked for his appearance, endures hardship and rejection. After a lonely winter, he discovers he has transformed into a beautiful swan. Accepted by a flock of swans, he finds belonging and self-acceptance, proving inner beauty shines through."
    },
    "The Princess and the Pea": {
        "author": "Hans Christian Andersen",
        "year": 1835,
        "summary": "A prince seeks a true princess to marry. A girl claiming to be a princess arrives soaked from a storm. To test her, the queen places a pea under twenty mattresses. The girl’s sensitivity to the pea proves her royal nature, and she marries the prince."
    },
    "The Elves and the Shoemaker": {
        "author": "Jacob Grimm",
        "year": 1812,
        "summary": "A poor shoemaker receives help from elves who craft perfect shoes overnight, saving his business. Grateful, he and his wife make clothes for the elves. The elves, delighted by the gifts, leave to continue their good deeds elsewhere."
    },
    "Cinderella": {
        "author": "Marian Roalfe Cox",
        "year": 1893,
        "summary": "Cinderella, mistreated by her stepmother and stepsisters, dreams of a better life. A fairy godmother helps her attend a ball, where she wins the prince’s heart. Losing her glass slipper, she is later found by the prince, who marries her, and they live happily ever after."
    },
    "Little Red Riding Hood": {
        "author": "Unknown, 1992 adaptation",
        "year": 1992,
        "summary": "Little Red Riding Hood visits her grandmother, unaware a wolf has swallowed her and disguised himself as her. The wolf tries to trick Red, but she escapes, and a woodsman saves her grandmother. The wolf is defeated, and they live safely."
    },
    "Goldilocks and the Three Bears": {
        "author": "Robert Southey",
        "year": 1837,
        "summary": "Goldilocks wanders into the home of three bears, sampling their porridge, chairs, and beds. She falls asleep in Baby Bear’s bed. When the bears return, they find her. Startled, Goldilocks flees, learning to respect others’ property."
    },
    "The Little Mermaid": {
        "author": "Hans Christian Andersen",
        "year": 1837,
        "summary": "A mermaid falls in love with a human prince and trades her voice for legs to join him on land. Despite her sacrifices, the prince marries another. Heartbroken, she chooses to dissolve into sea foam rather than harm him, earning a chance at redemption."
    },
    "Hansel and Gretel": {
        "author": "Jacob and Wilhelm Grimm",
        "year": 1812,
        "summary": "Hansel and Gretel, abandoned in the woods, find a candy house owned by a witch who plans to eat them. They outsmart her, pushing her into her own oven, and escape with her treasures, reuniting with their father."
    },
    "The Snow Queen": {
        "author": "Hans Christian Andersen",
        "year": 1844,
        "summary": "The Snow Queen kidnaps young Kai, enchanting him with a mirror’s shard. His friend Gerda embarks on a perilous journey to rescue him. Through courage and love, Gerda frees Kai from the Snow Queen’s icy palace, and they return home together."
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_story = None
    story_details = None
    if request.method == "POST":
        selected_story = request.form.get("story")
        story_details = stories.get(selected_story, {"summary": "Story not found.", "author": "", "year": ""})
    return render_template("index.html", stories=stories, selected_story=selected_story, story_details=story_details)

if __name__ == "__main__":
    app.run(debug=True)
