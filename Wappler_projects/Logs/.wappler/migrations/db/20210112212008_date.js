
exports.up = function(knex) {
  return knex.schema
    .table('topics', function (table) {
      table.string('date_added');
    })
};

exports.down = function(knex) {
  return knex.schema
    .table('topics', function (table) {
      table.dropColumn('date_added');
    })
};
