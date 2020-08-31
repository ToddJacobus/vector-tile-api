from django.db import connection
from django.http import Http404, HttpResponse


def mvt_tiles(request, zoom, x, y):
    """view for main mvt endpoint"""
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT ST_AsMVT(tile)
            FROM (
                SELECT
                    id,
                    ST_AsMVTGeom(
                        geom,
                        TileBBox({zoom},{x},{y},4326)
                    )
                FROM
                    core_point
            ) AS tile
        """)
        tile = bytes(cursor.fetchone()[0])
        if not len(tile):
            raise Http404()
    return HttpResponse(tile, content_type='application/x-protobuf')