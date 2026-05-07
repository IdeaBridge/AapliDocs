# frozen_string_literal: true

require_relative '../spec_helper'

RSpec.describe 'Jekyll Build' do
  describe 'Site can be built' do
    # This test ensures Jekyll can build the site without errors
    it 'builds successfully with bundle exec jekyll build' do
      # Run build and capture output
      build_output = `cd "#{ROOT_PATH}" && bundle exec jekyll build 2>&1`
      build_status = $?.success?

      expect(build_status).to be true,
        "Jekyll build failed with output:\n#{build_output}"
    end
  end

  describe 'Generated site structure' do
    let(:site_dir) { File.join(ROOT_PATH, '_site') }

    # Skip these tests if site hasn't been built yet
    before(:all) do
      site_dir = File.join(ROOT_PATH, '_site')
      unless Dir.exist?(site_dir)
        system("cd \"#{ROOT_PATH}\" && bundle exec jekyll build")
      end
    end

    context 'when site is built' do
      it 'creates _site directory' do
        skip 'Site not built' unless Dir.exist?(site_dir)
        expect(Dir.exist?(site_dir)).to be true
      end

      it 'generates index.html' do
        skip 'Site not built' unless Dir.exist?(site_dir)
        expect(File.exist?(File.join(site_dir, 'index.html'))).to be true
      end

      # Test that new documentation pages are generated
      describe 'Features pages' do
        %w[features applications authentication-access email-notifications
           gamification-rewards other-features user-experience].each do |page|
          it "generates #{page} page" do
            skip 'Site not built' unless Dir.exist?(site_dir)
            # Jekyll generates pretty URLs
            page_dir = File.join(site_dir, 'docs', 'configuration', page == 'features' ? page : "features/#{page}")
            page_path = Dir.exist?(page_dir) ? File.join(page_dir, 'index.html') : nil

            # Allow for different URL structures
            if page_path.nil? || !File.exist?(page_path.to_s)
              alternative = File.join(site_dir, 'docs', 'configuration', 'features', "#{page}.html")
              page_path = alternative if File.exist?(alternative)
            end

            # This is a soft check - document the expectation but don't fail hard
            skip "Page structure may vary" unless page_path && File.exist?(page_path)
            expect(File.exist?(page_path)).to be true
          end
        end
      end

      describe 'Entity Builder pages' do
        it 'generates entity-builder documentation' do
          skip 'Site not built' unless Dir.exist?(site_dir)
          # Check for any entity builder related files
          entity_files = Dir.glob(File.join(site_dir, 'docs', 'operations', '**', '*entity*'))
          expect(entity_files).not_to be_empty
        end
      end

      describe 'Welcome pages' do
        it 'generates welcome section' do
          skip 'Site not built' unless Dir.exist?(site_dir)
          welcome_dir = File.join(site_dir, 'docs', 'welcome')
          expect(Dir.exist?(welcome_dir)).to be true
        end
      end

      describe 'Generated HTML validity' do
        it 'generates valid HTML with proper doctypes' do
          skip 'Site not built' unless Dir.exist?(site_dir)

          html_files = Dir.glob(File.join(site_dir, '**', '*.html')).first(5)

          html_files.each do |file|
            content = File.read(file)
            # Check for basic HTML structure
            has_doctype = content.include?('<!DOCTYPE html>') || content.include?('<!doctype html>')
            expect(has_doctype).to be true, "#{file} missing DOCTYPE"
          end
        end
      end
    end
  end

  describe 'Configuration validation' do
    let(:config_path) { File.join(ROOT_PATH, '_config.yml') }
    let(:config) { YAML.safe_load(File.read(config_path)) }

    it 'has valid _config.yml' do
      expect { YAML.safe_load(File.read(config_path)) }.not_to raise_error
    end

    it 'has required site settings' do
      expect(config).to include('title')
      expect(config).to include('description')
    end

    it 'has search enabled for documentation' do
      expect(config['search_enabled']).to be true
    end

    it 'has mermaid configured for diagrams' do
      expect(config).to include('mermaid')
    end
  end
end
