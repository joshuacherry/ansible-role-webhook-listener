# encoding: utf-8

# extend tests with metadata
control '01' do
  impact 1.0
  title 'Verify webhook-listener service'
  desc 'Ensures webhook-listener service is up and running'
  describe service('webhook-listener') do
    it { should be_enabled }
    it { should be_installed }
    it { should be_running }
  end
end

control '02' do
  impact 1.0
  title 'Verify webhook-listener log file'
  desc 'Ensures logfile exists in an expected state'
  describe file('/var/log/webhook-listener.log') do
    it { should be_file }
    its('content') { should match /\[INFO \]  Repository .* successfully initialized/ }
    its('content') { should match /\[INFO \]  Listening for http connections/ }

  end

end
