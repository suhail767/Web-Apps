
exports.up = function(knex) {
  return knex('topics').where('id', 1).update({"entry":"Chess is a recreational game","topic":"Chess"})
    .then(() => {return knex('topics').where('id', 2).update({"entry":"Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury."})})
};

exports.down = function(knex) {
};
