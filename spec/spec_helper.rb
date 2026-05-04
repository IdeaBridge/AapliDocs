# frozen_string_literal: true

require 'yaml'
require 'rspec'
require 'date'
require 'time'

# Root path for the project
ROOT_PATH = File.expand_path('..', __dir__)

# Helper methods for documentation tests
module DocumentationHelpers
  # Get all markdown files in docs directory
  def self.all_doc_files
    Dir.glob(File.join(ROOT_PATH, 'docs', '**', '*.md'))
  end

  # Get all new/modified doc files from current branch (compared to main)
  def self.branch_doc_files
    # Get files changed compared to main branch
    changed_files = `git diff main --name-only`.split("\n")
    changed_files
      .select { |f| f.end_with?('.md') && f.start_with?('docs/') }
      .map { |f| File.join(ROOT_PATH, f) }
      .select { |f| File.exist?(f) }
  end

  # Get all image files in assets/images
  def self.all_image_files
    Dir.glob(File.join(ROOT_PATH, 'assets', 'images', '**', '*'))
       .select { |f| File.file?(f) }
  end

  # Get new image files from current branch
  def self.branch_image_files
    changed_files = `git diff main --name-only`.split("\n")
    changed_files
      .select { |f| f.start_with?('assets/images/') && !File.directory?(File.join(ROOT_PATH, f)) }
      .map { |f| File.join(ROOT_PATH, f) }
      .select { |f| File.exist?(f) }
  end

  # Parse YAML frontmatter from a markdown file
  def self.parse_frontmatter(file_path)
    content = File.read(file_path)
    return nil unless content.start_with?('---')

    yaml_end = content.index('---', 3)
    return nil unless yaml_end

    yaml_content = content[3...yaml_end].strip
    YAML.safe_load(yaml_content, permitted_classes: [::Date, ::Time])
  rescue Psych::SyntaxError => e
    raise "Invalid YAML in #{file_path}: #{e.message}"
  end

  # Extract image references from markdown content
  def self.extract_image_references(file_path)
    content = File.read(file_path)
    images = []

    # Match {% include image.html file="..." %}
    content.scan(/\{%\s*include\s+image\.html\s+file="([^"]+)"/).each do |match|
      images << match[0]
    end

    # Match standard markdown images ![alt](path)
    content.scan(/!\[.*?\]\(([^)]+)\)/).each do |match|
      images << match[0]
    end

    # Match HTML img tags
    content.scan(/<img[^>]+src="([^"]+)"/).each do |match|
      images << match[0]
    end

    images.uniq
  end

  # Get the parent document title for validation
  def self.find_parent_doc(parent_title)
    all_doc_files.find do |file|
      frontmatter = parse_frontmatter(file)
      frontmatter && frontmatter['title'] == parent_title
    end
  end

  # Valid layouts for the theme
  VALID_LAYOUTS = %w[default home page post about minimal].freeze

  # Required frontmatter fields for different document types
  REQUIRED_FIELDS = %w[layout title].freeze
end

RSpec.configure do |config|
  config.include DocumentationHelpers

  config.expect_with :rspec do |expectations|
    expectations.include_chain_clauses_in_custom_matcher_descriptions = true
  end

  config.mock_with :rspec do |mocks|
    mocks.verify_partial_doubles = true
  end

  config.shared_context_metadata_behavior = :apply_to_host_groups
  config.filter_run_when_matching :focus
  config.example_status_persistence_file_path = 'spec/examples.txt'
  config.disable_monkey_patching!
  config.warnings = true

  config.default_formatter = 'doc' if config.files_to_run.one?

  config.order = :random
  Kernel.srand config.seed
end
