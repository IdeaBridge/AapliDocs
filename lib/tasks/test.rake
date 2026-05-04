# frozen_string_literal: true

require 'rspec/core/rake_task'

namespace :spec do
  desc 'Run all documentation tests'
  RSpec::Core::RakeTask.new(:all) do |t|
    t.pattern = 'spec/**/*_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run frontmatter validation tests'
  RSpec::Core::RakeTask.new(:frontmatter) do |t|
    t.pattern = 'spec/documentation/frontmatter_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run image asset tests'
  RSpec::Core::RakeTask.new(:images) do |t|
    t.pattern = 'spec/documentation/images_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run navigation structure tests'
  RSpec::Core::RakeTask.new(:navigation) do |t|
    t.pattern = 'spec/documentation/navigation_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run content validation tests'
  RSpec::Core::RakeTask.new(:content) do |t|
    t.pattern = 'spec/documentation/content_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run build validation tests'
  RSpec::Core::RakeTask.new(:build) do |t|
    t.pattern = 'spec/documentation/build_spec.rb'
    t.rspec_opts = '--format documentation'
  end

  desc 'Run only branch-specific tests (for CI on PR)'
  RSpec::Core::RakeTask.new(:branch) do |t|
    t.pattern = 'spec/documentation/{frontmatter,images,navigation,content}_spec.rb'
    t.rspec_opts = '--format documentation'
  end
end

desc 'Run all tests'
task spec: 'spec:all'

# Default test task
task test: :spec
