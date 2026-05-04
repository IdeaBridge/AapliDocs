# frozen_string_literal: true

require_relative '../spec_helper'

RSpec.describe 'Documentation Content' do
  BRANCH_DOC_FILES = DocumentationHelpers.branch_doc_files

  describe 'Content quality for new documents' do
    BRANCH_DOC_FILES.each do |file_path|
      relative_path = file_path.sub("#{ROOT_PATH}/", '')
      content = File.read(file_path)
      frontmatter = DocumentationHelpers.parse_frontmatter(file_path)

      # Skip if no frontmatter
      next unless frontmatter

      context relative_path.to_s do
        it 'has content after frontmatter' do
          # Extract content after frontmatter
          yaml_end = content.index('---', 3)
          body = content[yaml_end + 3..].strip if yaml_end

          expect(body).not_to be_empty, "Document should have content after frontmatter"
        end

        it 'has no placeholder text' do
          placeholders = ['TODO', 'FIXME', 'XXX', 'Lorem ipsum', '[INSERT', 'TBD']
          placeholders.each do |placeholder|
            expect(content).not_to include(placeholder),
              "Document contains placeholder text: #{placeholder}"
          end
        end

        it 'has proper heading hierarchy' do
          # Extract headings
          headings = content.scan(/^(\#{1,6})\s+/)  
          next if headings.empty?

          # First heading after frontmatter should be h1 or h2
          first_heading_level = headings.first[0].length
          expect(first_heading_level).to be <= 2,
            "First heading should be h1 or h2, got h#{first_heading_level}"
        end

        it 'uses proper markdown syntax for links' do
          # Check for broken link syntax (missing bracket or parenthesis)
          broken_links = content.scan(/\[[^\]]*\]\s*[^(]/)
          expect(broken_links).to be_empty, "Found broken link syntax: #{broken_links.join(', ')}"
        end

        it 'has consistent use of image includes' do
          # If using {% include image.html %}, should have required attributes
          image_includes = content.scan(/\{%\s*include\s+image\.html[^%]*%\}/)

          image_includes.each do |include_tag|
            expect(include_tag).to include('file='),
              "Image include should have file attribute: #{include_tag}"
          end
        end

        it 'has appropriate content length' do
          yaml_end = content.index('---', 3)
          body = content[yaml_end + 3..].strip if yaml_end
          word_count = body.to_s.split.length

          expect(word_count).to be > 10,
            "Document seems too short (#{word_count} words). Consider adding more content."
        end
      end
    end
  end

  # Test specific documentation sections for completeness
  describe 'Features documentation completeness' do
    let(:features_dir) { File.join(ROOT_PATH, 'docs', 'configuration', 'features') }

    expected_features = [
      { file: 'applications_features.md', title: 'General Applications' },
      { file: 'authentication_access_features.md', title: 'Authentication & Access' },
      { file: 'email_notifications_features.md', title: 'E-mail & Notifications' },
      { file: 'gamification_rewards_features.md', title: 'Gamification & Rewards' },
      { file: 'other_features.md', title: 'Other Features' },
      { file: 'user_experience_features.md', title: 'User Experience' }
    ]

    expected_features.each do |feature|
      context feature[:file] do
        let(:file_path) { File.join(features_dir, feature[:file]) }

        it 'exists' do
          expect(File.exist?(file_path)).to be true
        end

        it 'has correct title' do
          if File.exist?(file_path)
            fm = DocumentationHelpers.parse_frontmatter(file_path)
            expect(fm['title']).to eq(feature[:title])
          end
        end

        it 'has Features as parent' do
          if File.exist?(file_path)
            fm = DocumentationHelpers.parse_frontmatter(file_path)
            expect(fm['parent']).to eq('Features')
          end
        end
      end
    end
  end

  describe 'Entity Builder documentation completeness' do
    let(:entity_dir) { File.join(ROOT_PATH, 'docs', 'operations', 'entity_builder') }

    expected_sections = [
      { file: 'entity_creation.md', title: 'Entity Creation' },
      { file: 'entity_datatypes.md', title: 'Data Types' },
      { file: 'entity_properties.md', title: 'Properties' },
      { file: 'entity_relationships.md', title: 'Relationships' }
    ]

    expected_sections.each do |section|
      context section[:file] do
        let(:file_path) { File.join(entity_dir, section[:file]) }

        it 'exists' do
          expect(File.exist?(file_path)).to be true
        end

        it 'has Entity Builder as parent' do
          if File.exist?(file_path)
            fm = DocumentationHelpers.parse_frontmatter(file_path)
            expect(fm['parent']).to eq('Entity Builder')
          end
        end
      end
    end
  end

  describe 'Welcome documentation completeness' do
    let(:welcome_dir) { File.join(ROOT_PATH, 'docs', 'welcome') }

    expected_sections = [
      { file: 'login.md', title: 'Logging into Aapli' },
      { file: 'create_account.md', title: 'Create Account' },
      { file: 'homepage.md', title: 'Homepage' }
    ]

    expected_sections.each do |section|
      context section[:file] do
        let(:file_path) { File.join(welcome_dir, section[:file]) }

        it 'exists' do
          expect(File.exist?(file_path)).to be true
        end

        it 'has Welcome to Aapli! as parent' do
          if File.exist?(file_path)
            fm = DocumentationHelpers.parse_frontmatter(file_path)
            expect(fm['parent']).to eq('Welcome to Aapli!')
          end
        end
      end
    end
  end

  describe 'Integrations documentation completeness' do
    let(:integrations_dir) { File.join(ROOT_PATH, 'docs', 'configuration', 'Integrations') }

    it 'has MS Teams integration documentation' do
      ms_teams_file = File.join(integrations_dir, 'ms_teams_integration.md')
      expect(File.exist?(ms_teams_file)).to be true
    end

    it 'MS Teams integration has Integrations as parent' do
      ms_teams_file = File.join(integrations_dir, 'ms_teams_integration.md')
      if File.exist?(ms_teams_file)
        fm = DocumentationHelpers.parse_frontmatter(ms_teams_file)
        expect(fm['parent']).to eq('Integrations')
      end
    end
  end

  describe 'Operations new sections completeness' do
    %w[entities email_logs failed_submissions].each do |section|
      context section do
        let(:section_dir) { File.join(ROOT_PATH, 'docs', 'operations', section) }
        let(:main_file) { File.join(section_dir, "#{section}.md") }

        it 'has main documentation file' do
          expect(File.exist?(main_file)).to be true
        end

        it 'main file has Operations as parent' do
          if File.exist?(main_file)
            fm = DocumentationHelpers.parse_frontmatter(main_file)
            expect(fm['parent']).to eq('Operations')
          end
        end
      end
    end
  end
end
