from couchdb.design import ViewDefinition


def add_index_options(doc):
    doc['options'] = {'local_seq': True}


def sync_design(db):
    views = [j for i, j in globals().items() if "_view" in i]
    ViewDefinition.sync_many(db, views, callback=add_index_options)


numbers_list_view = ViewDefinition('numbers', 'list_numbers', '''function(doc) {
  if(doc.doc_type == 'Number') {
    var cities_set = [];
    if ('city' in doc){ cities_set.push(doc['city']);}
    var age_set = [];
    if ('age' in doc){ age_set.push(doc['age']);}
    var images_set = [];
    for(i=0; i<doc['posts'].length; i++) {
        if ('city' in doc['posts'][i] && !!doc['posts'][i]['city']) {
            if (cities_set.indexOf(doc['posts'][i]['city']) >= 0) {
            }
            else {
                cities_set.push(doc['posts'][i]['city']);
            }
        }
        if ('age' in doc['posts'][i] && !!doc['posts'][i]['age']) {
            if (age_set.indexOf(doc['posts'][i]['age']) >= 0) {
            }
            else {
                age_set.push(doc['posts'][i]['age']);
            }
        }
        if ('images' in doc['posts'][i]) {
            for(j=0; j<doc['posts'][i]['images'].length; j++) {
                if(doc['posts'][i]['images'][j].link){
                    if (images_set.indexOf(doc['posts'][i]['images'][j].link) >= 0) {
                    }
                    else {
                        images_set.push(doc['posts'][i]['images'][j].link);
                    }
                }
            }
        }
    }
    var date = doc['last_post_date'].slice(0, 21);
    if (images_set.length == 0) {images_set.push('tits.png');}
    emit(date, {
        'id': doc['_id'],
        'last_post_date': doc['last_post_date'],
        'first_post_date': doc['posts'][0]['date_post'],
        'posts_length': doc['posts'].length,
        'cities_length': cities_set.length,
        'first_city': cities_set[0],
        'ages_length': age_set.length,
        'first_age': age_set[0],
        'images_length': images_set.length,
        'first_image': images_set[0]
        });
  }
}''')

VIEW_MAP = {
    u'_all_': numbers_list_view,
}
