PGDMP     
    *                |            Unplug    14.2    14.2 +               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    26958    Unplug    DATABASE     l   CREATE DATABASE "Unplug" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Unplug";
                postgres    false            �            1259    27047    Menu    TABLE     ~   CREATE TABLE public."Menu" (
    "Id" integer NOT NULL,
    "RestaurantId" integer,
    "CreatedAt" time without time zone
);
    DROP TABLE public."Menu";
       public         heap    postgres    false            �            1259    26961 	   MenuGroup    TABLE        CREATE TABLE public."MenuGroup" (
    "Id" integer NOT NULL,
    "Name" text,
    "SortOrder" integer,
    "MenuId" integer
);
    DROP TABLE public."MenuGroup";
       public         heap    postgres    false            �            1259    26992    MenuGroupItemMap    TABLE     r   CREATE TABLE public."MenuGroupItemMap" (
    "MenuGroupId" integer NOT NULL,
    "MenuItemId" integer NOT NULL
);
 &   DROP TABLE public."MenuGroupItemMap";
       public         heap    postgres    false            �            1259    26991     MenuGroupItemMap_MenuGroupId_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuGroupItemMap_MenuGroupId_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public."MenuGroupItemMap_MenuGroupId_seq";
       public          postgres    false    214                       0    0     MenuGroupItemMap_MenuGroupId_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public."MenuGroupItemMap_MenuGroupId_seq" OWNED BY public."MenuGroupItemMap"."MenuGroupId";
          public          postgres    false    213            �            1259    26960    MenuGroup_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuGroup_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."MenuGroup_Id_seq";
       public          postgres    false    210                       0    0    MenuGroup_Id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public."MenuGroup_Id_seq" OWNED BY public."MenuGroup"."Id";
          public          postgres    false    209            �            1259    26968    MenuItem    TABLE     �   CREATE TABLE public."MenuItem" (
    "Id" integer NOT NULL,
    "Name" text,
    "Description" text,
    "StockStatus" text,
    "RestaurantId" integer,
    "Image" text,
    "Ranking" integer,
    "Price" numeric,
    "Calorie" numeric
);
    DROP TABLE public."MenuItem";
       public         heap    postgres    false            �            1259    26967    MenuItem_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuItem_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."MenuItem_Id_seq";
       public          postgres    false    212                        0    0    MenuItem_Id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."MenuItem_Id_seq" OWNED BY public."MenuItem"."Id";
          public          postgres    false    211            �            1259    27046    Menu_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."Menu_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public."Menu_Id_seq";
       public          postgres    false    218            !           0    0    Menu_Id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public."Menu_Id_seq" OWNED BY public."Menu"."Id";
          public          postgres    false    217            �            1259    27018 
   Restaurant    TABLE     Q   CREATE TABLE public."Restaurant" (
    "Id" integer NOT NULL,
    "Name" text
);
     DROP TABLE public."Restaurant";
       public         heap    postgres    false            �            1259    27017    Restaurant_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."Restaurant_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public."Restaurant_Id_seq";
       public          postgres    false    216            "           0    0    Restaurant_Id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."Restaurant_Id_seq" OWNED BY public."Restaurant"."Id";
          public          postgres    false    215            s           2604    27050    Menu Id    DEFAULT     h   ALTER TABLE ONLY public."Menu" ALTER COLUMN "Id" SET DEFAULT nextval('public."Menu_Id_seq"'::regclass);
 :   ALTER TABLE public."Menu" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    218    217    218            p           2604    26964    MenuGroup Id    DEFAULT     r   ALTER TABLE ONLY public."MenuGroup" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuGroup_Id_seq"'::regclass);
 ?   ALTER TABLE public."MenuGroup" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    210    209    210            q           2604    26971    MenuItem Id    DEFAULT     p   ALTER TABLE ONLY public."MenuItem" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuItem_Id_seq"'::regclass);
 >   ALTER TABLE public."MenuItem" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    211    212    212            r           2604    27021    Restaurant Id    DEFAULT     t   ALTER TABLE ONLY public."Restaurant" ALTER COLUMN "Id" SET DEFAULT nextval('public."Restaurant_Id_seq"'::regclass);
 @   ALTER TABLE public."Restaurant" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    215    216    216                      0    27047    Menu 
   TABLE DATA           C   COPY public."Menu" ("Id", "RestaurantId", "CreatedAt") FROM stdin;
    public          postgres    false    218   �1                 0    26961 	   MenuGroup 
   TABLE DATA           J   COPY public."MenuGroup" ("Id", "Name", "SortOrder", "MenuId") FROM stdin;
    public          postgres    false    210   �1                 0    26992    MenuGroupItemMap 
   TABLE DATA           I   COPY public."MenuGroupItemMap" ("MenuGroupId", "MenuItemId") FROM stdin;
    public          postgres    false    214   m2                 0    26968    MenuItem 
   TABLE DATA           �   COPY public."MenuItem" ("Id", "Name", "Description", "StockStatus", "RestaurantId", "Image", "Ranking", "Price", "Calorie") FROM stdin;
    public          postgres    false    212   S3                 0    27018 
   Restaurant 
   TABLE DATA           4   COPY public."Restaurant" ("Id", "Name") FROM stdin;
    public          postgres    false    216   d@       #           0    0     MenuGroupItemMap_MenuGroupId_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public."MenuGroupItemMap_MenuGroupId_seq"', 1, false);
          public          postgres    false    213            $           0    0    MenuGroup_Id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."MenuGroup_Id_seq"', 1, false);
          public          postgres    false    209            %           0    0    MenuItem_Id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."MenuItem_Id_seq"', 1, false);
          public          postgres    false    211            &           0    0    Menu_Id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public."Menu_Id_seq"', 7, true);
          public          postgres    false    217            '           0    0    Restaurant_Id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Restaurant_Id_seq"', 7, true);
          public          postgres    false    215            y           2606    26997 &   MenuGroupItemMap MenuGroupItemMap_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_pkey" PRIMARY KEY ("MenuGroupId", "MenuItemId");
 T   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_pkey";
       public            postgres    false    214    214            u           2606    26999    MenuGroup MenuGroup_Id_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public."MenuGroup"
    ADD CONSTRAINT "MenuGroup_Id_key" UNIQUE ("Id");
 H   ALTER TABLE ONLY public."MenuGroup" DROP CONSTRAINT "MenuGroup_Id_key";
       public            postgres    false    210            w           2606    27011    MenuItem MenuItem_Id_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_Id_key" UNIQUE ("Id");
 F   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_Id_key";
       public            postgres    false    212            }           2606    27052    Menu Menu_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public."Menu"
    ADD CONSTRAINT "Menu_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY public."Menu" DROP CONSTRAINT "Menu_pkey";
       public            postgres    false    218            {           2606    27025    Restaurant Restaurant_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Restaurant"
    ADD CONSTRAINT "Restaurant_pkey" PRIMARY KEY ("Id");
 H   ALTER TABLE ONLY public."Restaurant" DROP CONSTRAINT "Restaurant_pkey";
       public            postgres    false    216            �           2606    27005 2   MenuGroupItemMap MenuGroupItemMap_MenuGroupId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey" FOREIGN KEY ("MenuGroupId") REFERENCES public."MenuGroup"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 `   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey";
       public          postgres    false    210    3189    214            �           2606    27214 1   MenuGroupItemMap MenuGroupItemMap_MenuItemId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey" FOREIGN KEY ("MenuItemId") REFERENCES public."MenuItem"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 _   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey";
       public          postgres    false    212    214    3191            ~           2606    27117    MenuGroup MenuGroup_MenuId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroup"
    ADD CONSTRAINT "MenuGroup_MenuId_fkey" FOREIGN KEY ("MenuId") REFERENCES public."Menu"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 M   ALTER TABLE ONLY public."MenuGroup" DROP CONSTRAINT "MenuGroup_MenuId_fkey";
       public          postgres    false    3197    210    218                       2606    27161 #   MenuItem MenuItem_RestaurantId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_RestaurantId_fkey" FOREIGN KEY ("RestaurantId") REFERENCES public."Restaurant"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 Q   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_RestaurantId_fkey";
       public          postgres    false    212    3195    216            �           2606    27112    Menu Menu_RestaurantId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Menu"
    ADD CONSTRAINT "Menu_RestaurantId_fkey" FOREIGN KEY ("RestaurantId") REFERENCES public."Restaurant"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 I   ALTER TABLE ONLY public."Menu" DROP CONSTRAINT "Menu_RestaurantId_fkey";
       public          postgres    false    216    218    3195               !   x�3�4�44�26�2��3�4602����� 9�<         �   x�-��
�0E�7_@�w�T�)t�f�A��B&��7�,�qνZ�`���	���y�9S�11T[���N����6ʑ����q�Ô�7�6Z�=XLk&�k.W\K�
X�{�i�ߌ�cd�)��V t��;�[�U��g!�*Z,�         �   x�U���0�sTLF����_G���l1�ۋ4�r� J��	�J�(�f�bL����� �	��q� =ہ��X��r�b��j�����D��� ���n��ٸ��@�BR������:�d@��{��T�Ѹk Գu��g�~o{��cʴD��72�r��U���x��z�(	� ��B�7�F8cMak_��Z�~���           x��Z�r�F}�l�Vʩ
��u�l%�[�j�J^R�5$"��"���{��H��:k?�e�Р�t���zA���,��m�K!
��/�%��x/�o������hS�^Թh�R��]�[���۲_Ӧ.���:ǇUE�b��>��e�UC.�A_�n����e&8��t�
�/h����\�C�u�;�#���	��J����f|��+�}Ӗ+�X������@�m���5��:n>����#?������oILz��~�9��37p��\^���ϗ?�&~@��,HI���<�P@���(���o}'�����R���ܡ�о� ���^�����U��W \�!g���빗����$<�S�c^H^�BT�����!+�5�M���uY�����A`�X���q1y�4�2�Y�\	�55��A�E�3�Zݰ���r�QC����f��}
$u@Y�:�46g:���r&J�"K��	��p�,��2�]'��<���'Yl2)&^t��������c�|�Ϻ̮E=��#�S���
��7M�������b�w�S�Q��%;R�]����>�:�� i���z��@3�V�6.s���w������X�����PSH��Z��v�ȱ���`/"��xcp�+��������\3��nE�,�J��fe�kɭ;k���܀G�Fu�w��N¶��!o|7uً���E�~��7y��%�Oމ���W�7H&8�ٰY�va��q*W-�H���EOj��*� Fn�Hܵ��"�GY��d�&iLY9^i�}�b����W5�C[����'����҈Pm�����K���;)o�`�����L(�ƀ�m6b�$p�>��s^u�>����{#/?��ǋ�G���^<��_\x(�4�I|y-O� ��k.sJ=`#/O[�V؛�և�H���{3V�n���7���ί��|��� �|�T��-����{/xK�]/��v�c,�^^��aO�w�t=OC���#�$i|�6����kE�t�]�ق�;��a+��_�[,|+��@C�y��>Ⱥ!��h�˖��]7V�V���N�]���_V�=�u=$�!n��U�E�F=&�$c�%:�:�7���0�bD�"�%\��}	�@r����5mH����V�^��S�7CՃyY��ޭg�����J|��,g��3��}W_<��|�4��"�Hd��ڡt�!�.��cX :fxzlvr�Q�}!e,���S=��:�"�'���3�\:e���6��ô�N{�ͬ4ue�$���FV�ȁJl��lW�!�!��s:��Y!�@I����<�۩��%/���7ru+��A�:e�H��l�����f���a]O؀;�v0�d����=��OT_E���s"oy������\r���e�QDhf
�?� [6GƷ�wB*d���7�b�ȕ<�=�L��dF�{1p�D%$�(%h�+��'Z;�.ƙx5�c5���50}>��>�8%�l�C�`&������Q,�3~{�ȹEP��牳,��,�I��w2���R?����4�~����%�c��	a��3�}��Z�np(���a�8��E��F6X:���c���5��z�ݖ{>{B{�sS�`�2T�DBƴ!�H�5jep�j��i�K!Y�mnk�@ѭ�Z�(�E���흓!�`�#�f`s8xKo��� �܊VOd���83�O~/6:g((!�M���/>Hn̥��4�۾,ʬDj�1MƼW#ۡrZ.�G-b����FE(L�8y�dY;��Y"�y��!Dbq3�g�I�x�p�{�d�N�W� ����� K�3�b!�K���B�jK耗�m��]��vb�}��L C��v��+K��a���P�=q�a��mD��Z�0w��W�E�w�>��ojS��ܦ�c���\�ؖ����(˪�����$�T�ٶ-o�ʵ+Ð�i�p`�&�y+PO*.v��Н!%9T���x��	{���<鞒5��Ǆ���hp@�vu�|��68y��������Ҟ��vpg���ؽ��|)�r���Pk� �F�L`"}ڇ]�m��;r��A3�g��]� �����U'k�E{U��q�'�����;����鴡��^����Y?�F��l�|���\��ӜJ���Ӳ�g��w8�`�v�|O���(a���y	C/�k��V.U_���p�]\K�ơR�d
�bm��ħ�i}#��J%���d'�����U�V��e��З�T92�y^����7n�����ۜ��LpW�P�m	��z���j��	5�Y�TI���R�q3s��r\�'�T@.�8䘋���Z��@8��S{�_��S�Eu�٫'[̛�ͨN�i�6�a�O5���� ���>"��&Hſi���k�E�5�&(�i�ý��	�hzh�J���7bu�d�9�B_��%����c�����3Ő�����QC3�cg��rG��Tzr1�ߦ��;���Z޳��f���˻G�g�9���u�;v���,0S��Ϊ脐����x�D)B��p�MY�'t�ؾ����i�{�s�A�� 4�����>��PhK��h�z�b�i"ԯ�m�� \�h:�8~jx!�˃X��cbF�`V�����_bgf1���n)��8M��^5�������(0�K6eu}Goץ�8�vC}������
�[��=�\���:���/��G"��b�	fQ�c�cy�1�ٵ ��ZC��7� �w��Dͮ��õ��3X����e�	�«�Hp�W��޲�P$���m��l�/�l. �O��2+�� D�)�Τ�OcF>��)Qxfx���£Z8k�:[oO~gðXՓ��d^�]|���wt���s��M���>�
�dD����ɦ�Ր�R_�%C�Z�2��2�*V.ϫ���ť��L���}�N~ehV���U3 �1m�M#e��R�}G����H+On��&�E�k|��7�>�e�� ��el;fz��T���\��2�]�=f��G�9?�5����4�i��b?r��-��܁uId��ԔyDY�����QD~�������@+y܋\y	���8rR,�0
�E�zb�(��	Q'ۯI�6��o��X���b���^^v���{Y���A�M�S'����E9K^D���Ϙ�qt:�#~���>����9�}�t�%�N���IB�9�2q#W��2Sz3<�#x�"��$�ㅾ� �OTr&͉��c�E�a�)sl�v��ٳ��F��            x�3�I-.	��Ңļ�=... U��     