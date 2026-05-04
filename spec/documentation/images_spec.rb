# frozen_string_literal: true

require_relative '../spec_helper'

RSpec.describe 'Image Assets' do
  # Image files introduced in this branch
  BRANCH_IMAGE_FILES = DocumentationHelpers.branch_image_files

  # All images referenced in documentation
  def self.all_referenced_images
    images = []
    DocumentationHelpers.branch_doc_files.each do |file|
      refs = DocumentationHelpers.extract_image_references(file)
      refs.each do |ref|
        images << { file: file, reference: ref }
      end
    end
    images
  end

  describe 'New image files from branch' do
    BRANCH_IMAGE_FILES.each do |file_path|
      relative_path = file_path.sub("#{ROOT_PATH}/", '')

      context "#{relative_path}" do
        it 'exists and is a valid file' do
          expect(File.exist?(file_path)).to be true
          expect(File.size(file_path)).to be > 0, "Image file should not be empty"
        end

        it 'has a valid image extension' do
          valid_extensions = %w[.png .jpg .jpeg .gif .svg .webp .ico]
          extension = File.extname(file_path).downcase
          expect(valid_extensions).to include(extension),
            "Image should have a valid extension, got: #{extension}"
        end

        it 'has a reasonable file size (under 2MB)' do
          max_size = 2 * 1024 * 1024 # 2MB
          expect(File.size(file_path)).to be < max_size,
            "Image file should be under 2MB for web performance"
        end

        it 'has a lowercase filename for consistency' do
          filename = File.basename(file_path)
          # Allow numbers but prefer lowercase letters
          expect(filename).to match(/^[a-z0-9_\-.]+$/i),
            "Filename should only contain alphanumeric characters, underscores, hyphens, and dots"
        end
      end
    end
  end

  describe 'Image references in documentation' do
    # Specific image files that should exist for new documentation
    new_images = [
      'addentity.png',
      'addrelation.png',
      'adminlogin26.png',
      'adminpanel26.png',
      'applicationadds.png',
      'authaccess.png',
      'authtype.png',
      'datadrag.png',
      'dataedit.png',
      'dataprops.png',
      'deltable.png',
      'dtypesearch.png',
      'ebdatatypes.png',
      'ebhome.png',
      'eboverview.png',
      'ebwidget.png',
      'editrel.png',
      'elogs.png',
      'elogwidget.png',
      'entities.png',
      'entitytable.png',
      'entwidget.png',
      'failsubs.png',
      'failsubwidget.png',
      'featuresscreen.png',
      'featureswidget.png',
      'genprop.png',
      'inactivity.png',
      'integrations.png',
      'newentable.png',
      'operations.png',
      'otherfeatures.png',
      'relsettings.png',
      'rewards.png',
      'singlesession.png',
      'smtpp1.png',
      'smtpp2.png',
      'so1.png',
      'so2.png',
      'so3.png',
      'so4.png',
      'so5.png',
      'so6.png',
      'so7.png',
      'so8.png',
      'so9.png',
      'teamspanel.png',
      'teamssettings.png',
      'userexp.png'
    ]

    new_images.each do |image_name|
      it "has #{image_name} in assets/images" do
        image_path = File.join(ROOT_PATH, 'assets', 'images', image_name)
        expect(File.exist?(image_path)).to(be(true),
          "Expected image #{image_name} to exist in assets/images/")
      end
    end
  end

  describe 'Image references validation' do
    all_referenced_images.each do |ref_info|
      doc_file = ref_info[:file].sub("#{ROOT_PATH}/", '')
      image_ref = ref_info[:reference]

      context "#{doc_file} -> #{image_ref}" do
        it 'references an existing image' do
          # Handle different reference formats
          if image_ref.start_with?('/')
            # Absolute path from root
            image_path = File.join(ROOT_PATH, image_ref)
          elsif image_ref.start_with?('http')
            # External URL - skip validation
            skip 'External URL - not validating'
          else
            # Relative path or just filename
            # Try assets/images first (common pattern for include image.html)
            image_path = File.join(ROOT_PATH, 'assets', 'images', image_ref)
            unless File.exist?(image_path)
              # Try relative to the doc file
              doc_dir = File.dirname(ref_info[:file])
              image_path = File.join(doc_dir, image_ref)
            end
          end

          expect(File.exist?(image_path)).to(be(true),
            "Image '#{image_ref}' referenced in #{doc_file} does not exist")
        end
      end
    end
  end

  describe 'Features section images' do
    features_images = %w[
      featureswidget.png
      featuresscreen.png
      authaccess.png
      authtype.png
      inactivity.png
      singlesession.png
      userexp.png
      rewards.png
      smtpp1.png
      smtpp2.png
      otherfeatures.png
    ]

    features_images.each do |image|
      it "has #{image} for features documentation" do
        path = File.join(ROOT_PATH, 'assets', 'images', image)
        expect(File).to exist(path)
      end
    end
  end

  describe 'Entity Builder section images' do
    entity_images = %w[
      ebwidget.png
      ebhome.png
      eboverview.png
      ebdatatypes.png
      dtypesearch.png
      addentity.png
      genprop.png
      dataprops.png
      datadrag.png
      dataedit.png
      newentable.png
      deltable.png
      entitytable.png
      addrelation.png
      relsettings.png
      editrel.png
    ]

    entity_images.each do |image|
      it "has #{image} for entity builder documentation" do
        path = File.join(ROOT_PATH, 'assets', 'images', image)
        expect(File).to exist(path)
      end
    end
  end

  describe 'Operations section images' do
    operations_images = %w[
      entwidget.png
      entities.png
      elogwidget.png
      elogs.png
      failsubwidget.png
      failsubs.png
    ]

    operations_images.each do |image|
      it "has #{image} for operations documentation" do
        path = File.join(ROOT_PATH, 'assets', 'images', image)
        expect(File).to exist(path)
      end
    end
  end

  describe 'Integrations section images' do
    integrations_images = %w[
      integrations.png
      teamssettings.png
      teamspanel.png
    ]

    integrations_images.each do |image|
      it "has #{image} for integrations documentation" do
        path = File.join(ROOT_PATH, 'assets', 'images', image)
        expect(File).to exist(path)
      end
    end
  end
end
