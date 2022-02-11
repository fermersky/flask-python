const path = require('path');
const async = require('async');
const newman = require('newman');

const PARALLEL_RUN_COUNT = 40;

const parametersForTestRun = {
  collection: path.join(__dirname, 'tests.json'),
  iterationCount: 10,
  reporters: 'cli',
};

parallelCollectionRun = function (done) {
  newman.run(parametersForTestRun, done);
};

let commands = [];
for (let index = 0; index < PARALLEL_RUN_COUNT; index++) {
  commands.push(parallelCollectionRun);
}

async.parallel(commands, (err, results) => {
  err && console.error(err);

  results.forEach(function (result) {
    var failures = result.run.failures;
    console.info(
      failures.length ? JSON.stringify(failures.failures, null, 2) : `${result.collection.name} ran successfully.`
    );
  });
});
