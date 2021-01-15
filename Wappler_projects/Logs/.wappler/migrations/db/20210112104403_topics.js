
exports.up = function(knex) {
  return knex.schema
    .createTable('Topics', function (table) {
      table.increments('id');
      table.string('topic');
      table.string('entry');
    })
};

exports.down = function(knex) {
  return knex.schema
    .dropTable('Topics')
};
