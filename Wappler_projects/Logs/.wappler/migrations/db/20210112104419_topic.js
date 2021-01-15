
exports.up = function(knex) {
  return knex.schema
    .renameTable('Topics', 'topics')
};

exports.down = function(knex) {
  return knex.schema
    .renameTable('topics', 'Topics')
};
