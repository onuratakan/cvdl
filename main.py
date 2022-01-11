


from CVMaker import *

if __name__ == '__main__':
    cv_maker = CVMaker(
        content_path='content.toml',
        schema_path='schemas.toml',
        design_path='design.toml',
        output_file_name='cv'
    )
    cv_maker.process_schema()
    cv_maker.process_content()
    cv_maker.process_style()
    cv_maker.generate_cv()
    cv_maker.render_cv()