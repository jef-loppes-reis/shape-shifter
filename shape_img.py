from os import path, mkdir

from PIL import Image, ImageDraw, UnidentifiedImageError

class ShapeShifterImg:
    """---"""
    colors = {
        'kaizen_blue': (0, 165, 172),
        'kaizen_gray': (35, 35, 36),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
    }

    def __init__(self, path_img:str) -> None:
        self.path_img = path_img
        self.name_photo = self.path_img.split('/')[-1] #if self.path_img.endswith(
#                    ['.jpg', '.png', '.JPG', '.JPEG', '.PNG']) else None
        # try:
        #     if path.exists(self.path_img):
        #         self.name_photo = path_img.split('/')[-1] if path_img.endswith(
        #             ['.jpg', '.png', '.JPG', '.JPEG', '.PNG']) else None
        # except Exception as e:
        #     raise RuntimeError("Erro, a foto nao existe!") from e


    def _draw_corner(self, empate:ImageDraw.ImageDraw, image:Image.Image, margin:int=5):
        """_summary_

        Args:
            draw (ImageDraw.ImageDraw): _description_
            image (Image.Image): _description_
            color (str, optional): _description_. Defaults to 'black'.
            margin (int, optional): _description_. Defaults to 5.
        """
        width, height = image.size
        min_size = min(width, height)
        shapes = [
            [(width - margin, margin), (width - margin - width*0.02, margin)],
            [(width - margin, margin), (width - margin, margin + min_size*0.02)],
            [(margin, height - margin), (margin, height - margin - min_size*0.02)],
            [(margin + min_size*0.02, height - margin), (margin, height - margin)],
        ]
        for shape in shapes:
            empate.line(shape, fill=self.colors['black'], width=1)

    def tratar(self, img_tratar: Image) -> None:
        """_summary_

        Args:
            img (Image): _description_
            colors (dict): _description_
        """
        background_color = self.colors['white']

        new_image = Image.new('RGB', (img_tratar.size[0]//5, img_tratar.size[1]//6), background_color)
        img_tratar.paste(im=new_image, box=(img_tratar.size[0] - new_image.size[0], 0))
        min_size = 1200 / min(img_tratar.size)
        return img_tratar.resize(
            (int(img_tratar.size[0] * min_size),
            int(img_tratar.size[1] * min_size)),
            Image.Resampling.BILINEAR
            )


    def check_size_img(self, codpro:str='000000', size_limit:int=500) -> dict:
        """_summary_

        Args:
            codpro (str, optional): _description_. Defaults to '000000'.

        Returns:
            dict: _description_
        """
        try:
            img_pil = Image.open(self.path_img)
            tam_img = img_pil.size
            if tam_img[0] < size_limit or tam_img[1] < size_limit:
                img = self.tratar(img_tratar=img_pil)
                draw = ImageDraw.Draw(img)
                self._draw_corner(empate=draw, image=img)
                if not path.exists('./out/photos_resize_1200x1200'):
                    mkdir('./out')
                    mkdir('./out/photos_resize_1200x1200')
                img.save(f'out/photos_resize_1200x1200/{self.name_photo}')
                return {
                    'codpro': codpro,
                    'name_photo': self.name_photo,
                    'resize': True,
                    'foto_corrompida': False
                }
            return {
                'codpro': codpro,
                'name_photo': self.name_photo,
                'resize': False,
                'foto_corrompida': False,
                'foto_size_limit': False
            }
        except UnidentifiedImageError:
            return {
                'codpro': codpro,
                'name_photo': self.name_photo,
                'resize': False,
                'foto_corrompida': True,
                'foto_size_limit': False
            }
        except Exception:
            return {
                'codpro': codpro,
                'name_photo': self.name_photo,
                'resize': False,
                'foto_corrompida': False,
                'foto_size_limit': True
            }
