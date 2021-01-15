
exports.up = function (knex) {
  return knex('topics').where('id', 1).update({ "entry": "Chess is a recreational and competitive board game played between two players. Sometimes called Western or international chess to distinguish it from its predecessors and other chess variants, the current form of the game emerged in Southern Europe during the second half of the 15th century after evolving from similar, much older games of Indian and Persian origin.", "topic": "Chess" })
};

exports.down = function (knex) {
};
