db = db.getSiblingDB("sentiments");

db.createCollection('containerizedTest');

db.sentiments.insertMany([
    {text: 'I am so happy and sad', isPositive: true, positive_words: ['happy', 'happy2'], negative_words: ['sad', 'sad2'], createdDate: '2022-12-01'},
    {text: 'I am so happy and sad sad', isPositive: false, positive_words: ['happy', 'happy2'], negative_words: ['sad', 'sad2'], createdDate: '2022-12-02'}
]);