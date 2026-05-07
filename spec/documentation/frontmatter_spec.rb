# frozen_string_literal: true

require_relative '../spec_helper'

RSpec.describe 'Documentation Frontmatter' do
  # Files introduced in this branch
  BRANCH_DOC_FILES = DocumentationHelpers.branch_doc_files

  describe 'New documentation files from branch' do
    BRANCH_DOC_FILES.each do |file_path|
      relative_path = file_path.sub("#{ROOT_PATH}/", '')

      context "#{relative_path}" do
        let(:frontmatter) { DocumentationHelpers.parse_frontmatter(file_path) }

        it 'has valid YAML frontmatter' do
          expect { DocumentationHelpers.parse_frontmatter(file_path) }.not_to raise_error
          expect(frontmatter).not_to be_nil, "File should have YAML frontmatter"
        end

        it 'has a layout field' do
          expect(frontmatter).to include('layout')
        end

        it 'has a valid layout value' do
          expect(DocumentationHelpers::VALID_LAYOUTS).to include(frontmatter['layout']),
            "Layout '#{frontmatter['layout']}' is not valid. Valid layouts: #{DocumentationHelpers::VALID_LAYOUTS.join(', ')}"
        end

        it 'has a title field' do
          expect(frontmatter).to include('title')
          expect(frontmatter['title']).not_to be_empty, "Title should not be empty"
        end

        it 'has nav_order if it has a parent' do
          if frontmatter['parent']
            expect(frontmatter).to include('nav_order'),
              "Documents with a parent should have nav_order for consistent navigation"
          end
        end

        it 'has has_children set if it is a parent document' do
          # Check if this document is referenced as a parent by other documents
          is_parent = BRANCH_DOC_FILES.any? do |other_file|
            next if other_file == file_path
            other_fm = DocumentationHelpers.parse_frontmatter(other_file)
            other_fm && other_fm['parent'] == frontmatter['title']
          end

          if is_parent
            expect(frontmatter['has_children']).to eq(true),
              "Document '#{frontmatter['title']}' is referenced as parent but has_children is not true"
          end
        end

        it 'references an existing parent document' do
          if frontmatter['parent']
            parent_doc = DocumentationHelpers.find_parent_doc(frontmatter['parent'])
            expect(parent_doc).not_to be_nil,
              "Parent '#{frontmatter['parent']}' does not exist"
          end
        end

        it 'references an existing grand_parent document' do
          if frontmatter['grand_parent']
            grandparent_doc = DocumentationHelpers.find_parent_doc(frontmatter['grand_parent'])
            expect(grandparent_doc).not_to be_nil,
              "Grand parent '#{frontmatter['grand_parent']}' does not exist"
          end
        end
      end
    end
  end

  # Specific tests for Features documentation
  describe 'Features documentation structure' do
    let(:features_dir) { File.join(ROOT_PATH, 'docs', 'configuration', 'features') }
    let(:features_files) { Dir.glob(File.join(features_dir, '*.md')) }

    it 'has a main features.md file' do
      expect(File.exist?(File.join(features_dir, 'features.md'))).to be true
    end

    it 'all feature files have Configurations as grand_parent' do
      features_files.each do |file|
        next if file.end_with?('features.md') # Skip the parent file

        frontmatter = DocumentationHelpers.parse_frontmatter(file)
        next unless frontmatter

        if frontmatter['parent'] == 'Features'
          expect(frontmatter['grand_parent']).to eq('Configurations'),
            "#{File.basename(file)} should have grand_parent: Configurations"
        end
      end
    end
  end

  # Specific tests for Entity Builder documentation
  describe 'Entity Builder documentation structure' do
    let(:entity_builder_dir) { File.join(ROOT_PATH, 'docs', 'operations', 'entity_builder') }
    let(:entity_builder_files) { Dir.glob(File.join(entity_builder_dir, '*.md')) }

    it 'has a main entity_builder.md file' do
      expect(File.exist?(File.join(entity_builder_dir, 'entity_builder.md'))).to be true
    end

    it 'all entity builder files have Operations as grand_parent' do
      entity_builder_files.each do |file|
        next if file.end_with?('entity_builder.md') # Skip the parent file

        frontmatter = DocumentationHelpers.parse_frontmatter(file)
        next unless frontmatter

        if frontmatter['parent'] == 'Entity Builder'
          expect(frontmatter['grand_parent']).to eq('Operations'),
            "#{File.basename(file)} should have grand_parent: Operations"
        end
      end
    end
  end

  # Specific tests for Welcome documentation
  describe 'Welcome documentation structure' do
    let(:welcome_dir) { File.join(ROOT_PATH, 'docs', 'welcome') }
    let(:welcome_files) { Dir.glob(File.join(welcome_dir, '*.md')) }

    it 'has a main welcome.md file' do
      expect(File.exist?(File.join(welcome_dir, 'welcome.md'))).to be true
    end

    it 'welcome.md is configured as a parent' do
      welcome_file = File.join(welcome_dir, 'welcome.md')
      frontmatter = DocumentationHelpers.parse_frontmatter(welcome_file)

      expect(frontmatter['has_children']).to be true
    end
  end

  # Specific tests for Integrations documentation
  describe 'Integrations documentation structure' do
    let(:integrations_dir) { File.join(ROOT_PATH, 'docs', 'configuration', 'Integrations') }
    let(:integrations_files) { Dir.glob(File.join(integrations_dir, '*.md')) }

    it 'has a main integrations.md file' do
      expect(File.exist?(File.join(integrations_dir, 'integrations.md'))).to be true
    end

    it 'integrations.md is configured as a parent' do
      integrations_file = File.join(integrations_dir, 'integrations.md')
      if File.exist?(integrations_file)
        frontmatter = DocumentationHelpers.parse_frontmatter(integrations_file)
        expect(frontmatter['has_children']).to be true
      end
    end
  end
end
