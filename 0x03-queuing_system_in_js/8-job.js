function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
      throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const newJob = queue.create('push_notification_code_2', job);
  
    newJob.on('enqueue', () => {
      console.log(`Notification job created: ${newJob.id}`);
    })
    .on('complete', () => {
        console.log(`Notification job ${newJob.id} completed`);
    })
    .on('failed', (err) => {
        console.log('Notification job', newJob.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
        console.log('Notification job', newJob.id, `${progress}% complete`);
    });
    newJob.save();
  });
};

export default createPushNotificationsJobs;