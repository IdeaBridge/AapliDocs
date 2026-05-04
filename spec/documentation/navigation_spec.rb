# frozen_string_literal: true

require_relative '../spec_helper'

RSpec.describe 'Navigation Structure' do
  # Get all documentation files
  let(:all_docs) do
    DocumentationHelpers.all_doc_files.map do |file|
      frontmatter = DocumentationHelpers.parse_frontmatter(file)
      { path: file, frontmatter: frontmatter } if frontmatter
    end.compact
  end

  # Get branch-specific docs
  let(:branch_docs) do
    DocumentationHelpers.branch_doc_files.map do |file|
      frontmatter = DocumentationHelpers.parse_frontmatter(file)
      { path: file, frontmatter: frontmatter } if frontmatter
    end.compact
  end

  describe 'Navigation hierarchy for new documents' do
    # Test Features section navigation
    context 'Features section' do
      let(:features_parent) do
        all_docs.find { |d| d[:frontmatter]['title'] == 'Features' && d[:frontmatter]['parent'] == 'Configurations' }
      end

      let(:features_children) do
        all_docs.select { |d| d[:frontmatter]['parent'] == 'Features' }
      end

      it 'has Features as a child of Configurations' do
        expect(features_parent).not_to be_nil
      end

      it 'Features parent has has_children set to true' do
        expect(features_parent[:frontmatter]['has_children']).to be true
      end

      it 'all Features children reference correct parent' do
        features_children.each do |child|
          expect(child[:frontmatter]['parent']).to eq('Features')
          expect(child[:frontmatter]['grand_parent']).to eq('Configurations')
        end
      end

      it 'Features children have unique nav_order values' do
        nav_orders = features_children.map { |c| c[:frontmatter]['nav_order'] }.compact
        expect(nav_orders.uniq.length).to eq(nav_orders.length),
          "Features children should have unique nav_order values"
      end
    end

    # Test Entity Builder section navigation
    context 'Entity Builder section' do
      let(:entity_builder_parent) do
        all_docs.find { |d| d[:frontmatter]['title'] == 'Entity Builder' && d[:frontmatter]['parent'] == 'Operations' }
      end

      let(:entity_builder_children) do
        all_docs.select { |d| d[:frontmatter]['parent'] == 'Entity Builder' }
      end

      it 'has Entity Builder as a child of Operations' do
        expect(entity_builder_parent).not_to be_nil
      end

      it 'Entity Builder parent has has_children set to true' do
        expect(entity_builder_parent[:frontmatter]['has_children']).to be true
      end

      it 'all Entity Builder children reference correct parent' do
        entity_builder_children.each do |child|
          expect(child[:frontmatter]['parent']).to eq('Entity Builder')
          expect(child[:frontmatter]['grand_parent']).to eq('Operations')
        end
      end
    end

    # Test Welcome section navigation
    context 'Welcome section' do
      let(:welcome_parent) do
        all_docs.find { |d| d[:frontmatter]['title'] == 'Welcome to Aapli!' }
      end

      let(:welcome_children) do
        all_docs.select { |d| d[:frontmatter]['parent'] == 'Welcome to Aapli!' }
      end

      it 'has Welcome section as top-level navigation' do
        expect(welcome_parent).not_to be_nil
        expect(welcome_parent[:frontmatter]['parent']).to be_nil
      end

      it 'Welcome parent has has_children set to true' do
        expect(welcome_parent[:frontmatter]['has_children']).to be true
      end

      it 'Welcome has appropriate nav_order for early visibility' do
        expect(welcome_parent[:frontmatter]['nav_order']).to be <= 5,
          "Welcome section should appear early in navigation"
      end
    end

    # Test Integrations section navigation
    context 'Integrations section' do
      let(:integrations_parent) do
        all_docs.find { |d| d[:frontmatter]['title'] == 'Integrations' && d[:frontmatter]['parent'] == 'Configurations' }
      end

      let(:integrations_children) do
        all_docs.select { |d| d[:frontmatter]['parent'] == 'Integrations' }
      end

      it 'has Integrations as a child of Configurations' do
        expect(integrations_parent).not_to be_nil
      end

      it 'Integrations parent has has_children set to true' do
        expect(integrations_parent[:frontmatter]['has_children']).to be true
      end
    end

    # Test new standalone sections (Entities, Email Logs, Failed Submissions)
    context 'New Operations sections' do
      %w[Entities E-mail\ Logs Failed\ Submissions].each do |section_name|
        context section_name do
          let(:section_doc) do
            all_docs.find { |d| d[:frontmatter]['title'] == section_name }
          end

          it "has #{section_name} section" do
            expect(section_doc).not_to be_nil, "Expected to find #{section_name} document"
          end

          it "#{section_name} is under Operations" do
            if section_doc
              expect(section_doc[:frontmatter]['parent']).to eq('Operations')
            end
          end
        end
      end
    end
  end

  describe 'Navigation consistency' do
    it 'no orphaned documents (all have parent or are top-level)' do
      branch_docs.each do |doc|
        fm = doc[:frontmatter]
        next if fm['nav_order'] && fm['parent'].nil? # Top-level document

        if fm['parent']
          parent = all_docs.find { |d| d[:frontmatter]['title'] == fm['parent'] }
          expect(parent).not_to be_nil,
            "Document '#{fm['title']}' references non-existent parent '#{fm['parent']}'"
        end
      end
    end

    it 'all parent documents have has_children: true' do
      parent_titles = branch_docs
        .map { |d| d[:frontmatter]['parent'] }
        .compact
        .uniq

      parent_titles.each do |title|
        parent_doc = all_docs.find { |d| d[:frontmatter]['title'] == title }
        if parent_doc
          expect(parent_doc[:frontmatter]['has_children']).to be(true),
            "Parent '#{title}' should have has_children: true"
        end
      end
    end

    it 'grand_parent references are valid' do
      branch_docs.each do |doc|
        fm = doc[:frontmatter]
        next unless fm['grand_parent']

        grandparent = all_docs.find { |d| d[:frontmatter]['title'] == fm['grand_parent'] }
        expect(grandparent).not_to be_nil,
          "Document '#{fm['title']}' references non-existent grand_parent '#{fm['grand_parent']}'"

        # Also verify the parent's parent is the grand_parent
        if fm['parent']
          parent = all_docs.find { |d| d[:frontmatter]['title'] == fm['parent'] }
          if parent
            expect(parent[:frontmatter]['parent']).to eq(fm['grand_parent']),
              "Grand parent chain is broken for '#{fm['title']}'"
          end
        end
      end
    end
  end
end
