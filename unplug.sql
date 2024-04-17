PGDMP     2    '                |            Unplug    14.2    14.2 !               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    26958    Unplug    DATABASE     l   CREATE DATABASE "Unplug" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Unplug";
                postgres    false            �            1259    26961 	   MenuGroup    TABLE     i   CREATE TABLE public."MenuGroup" (
    "Id" integer NOT NULL,
    "Name" text,
    "SortOrder" integer
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
       public          postgres    false    214                       0    0     MenuGroupItemMap_MenuGroupId_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public."MenuGroupItemMap_MenuGroupId_seq" OWNED BY public."MenuGroupItemMap"."MenuGroupId";
          public          postgres    false    213            �            1259    26960    MenuGroup_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuGroup_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."MenuGroup_Id_seq";
       public          postgres    false    210                       0    0    MenuGroup_Id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public."MenuGroup_Id_seq" OWNED BY public."MenuGroup"."Id";
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
       public          postgres    false    212                       0    0    MenuItem_Id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."MenuItem_Id_seq" OWNED BY public."MenuItem"."Id";
          public          postgres    false    211            �            1259    27018 
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
       public          postgres    false    216                       0    0    Restaurant_Id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."Restaurant_Id_seq" OWNED BY public."Restaurant"."Id";
          public          postgres    false    215            k           2604    26964    MenuGroup Id    DEFAULT     r   ALTER TABLE ONLY public."MenuGroup" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuGroup_Id_seq"'::regclass);
 ?   ALTER TABLE public."MenuGroup" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    210    209    210            l           2604    26971    MenuItem Id    DEFAULT     p   ALTER TABLE ONLY public."MenuItem" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuItem_Id_seq"'::regclass);
 >   ALTER TABLE public."MenuItem" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    212    211    212            m           2604    27021    Restaurant Id    DEFAULT     t   ALTER TABLE ONLY public."Restaurant" ALTER COLUMN "Id" SET DEFAULT nextval('public."Restaurant_Id_seq"'::regclass);
 @   ALTER TABLE public."Restaurant" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    216    215    216                      0    26961 	   MenuGroup 
   TABLE DATA           @   COPY public."MenuGroup" ("Id", "Name", "SortOrder") FROM stdin;
    public          postgres    false    210   �$                 0    26992    MenuGroupItemMap 
   TABLE DATA           I   COPY public."MenuGroupItemMap" ("MenuGroupId", "MenuItemId") FROM stdin;
    public          postgres    false    214   �%                 0    26968    MenuItem 
   TABLE DATA           �   COPY public."MenuItem" ("Id", "Name", "Description", "StockStatus", "RestaurantId", "Image", "Ranking", "Price", "Calorie") FROM stdin;
    public          postgres    false    212   {&       
          0    27018 
   Restaurant 
   TABLE DATA           4   COPY public."Restaurant" ("Id", "Name") FROM stdin;
    public          postgres    false    216   �3                  0    0     MenuGroupItemMap_MenuGroupId_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public."MenuGroupItemMap_MenuGroupId_seq"', 1, false);
          public          postgres    false    213                       0    0    MenuGroup_Id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."MenuGroup_Id_seq"', 1, false);
          public          postgres    false    209                       0    0    MenuItem_Id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."MenuItem_Id_seq"', 1, false);
          public          postgres    false    211                       0    0    Restaurant_Id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public."Restaurant_Id_seq"', 1, false);
          public          postgres    false    215            s           2606    26997 &   MenuGroupItemMap MenuGroupItemMap_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_pkey" PRIMARY KEY ("MenuGroupId", "MenuItemId");
 T   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_pkey";
       public            postgres    false    214    214            o           2606    26999    MenuGroup MenuGroup_Id_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public."MenuGroup"
    ADD CONSTRAINT "MenuGroup_Id_key" UNIQUE ("Id");
 H   ALTER TABLE ONLY public."MenuGroup" DROP CONSTRAINT "MenuGroup_Id_key";
       public            postgres    false    210            q           2606    27011    MenuItem MenuItem_Id_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_Id_key" UNIQUE ("Id");
 F   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_Id_key";
       public            postgres    false    212            u           2606    27025    Restaurant Restaurant_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Restaurant"
    ADD CONSTRAINT "Restaurant_pkey" PRIMARY KEY ("Id");
 H   ALTER TABLE ONLY public."Restaurant" DROP CONSTRAINT "Restaurant_pkey";
       public            postgres    false    216            v           2606    27005 2   MenuGroupItemMap MenuGroupItemMap_MenuGroupId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey" FOREIGN KEY ("MenuGroupId") REFERENCES public."MenuGroup"("Id") ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 `   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey";
       public          postgres    false    210    3183    214            w           2606    27012 1   MenuGroupItemMap MenuGroupItemMap_MenuItemId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey" FOREIGN KEY ("MenuItemId") REFERENCES public."MenuItem"("Id") NOT VALID;
 _   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey";
       public          postgres    false    214    3185    212               �   x���
�@�ϙ��/P�=��X�ൗ�"��-�~׽&��h��+����S�c�*�������b3���@�Fи��*0d���+�[M�q�,p�Õ�������ǐ��+�j�a�"1�X'C�[���q��2���{�*Y         �   x�U���0�wTL �d/鿎8����f2�i���?$ ��b�Q�� Ř8���j Ձc�8V���� �9�s�z�HT5~	�TR�I"`�ph�Xc�n���g�l�55Э���1��09��:�d@����!�n�Ѹk Իu���
���@�)���oʈȵ$W�jv�k��w�DI`H$���5�k
[����Z_����           x��Z�r�F}��b�j+eW��o�ۉ,[�r%/�� pq�V��=sJ��d�r�Ow�>ݠ�Ǯ�Y�2��5�`i����EӤe�W��U�zn}Z�uuO��'��g�#MA:v۴��`uN��%g]S��:�R΋u��j����uk֗�-3���=#i�Y� ��ʛr!�V�O[5C���J������d,M��o�rY֬"�a�:q�t�2�'+֖]�������O�u�����������k���:�C����O~����&���	n{�
��uVv}ې384C���?����9o���w���we�"M]6
��W��͆��� �r��"�y
!�H�(qD�u�EO߶l��{�nyg�?*�����a�N�5oo�=oY[�yÁ�52~����:�su�j�c'^bQ_�Xo�N�+�����A+�5$���=CƗ ���L���y�	<G?/�����'*����,��VU6�jh�e���O�$(�e��V�E���Ea�Y��4�;q�<���Y��)���$ٖ[l��g��3���雨���5�(ˍN�-
���]����<�<�:s��z�V\Po���e[T/Pu�Ym��ߛ{�b�
�w˗�R �N 9Xd"�G�dh���Zb�Nc��5�T|�^7��� YY�Z0���W�*�[�i��P��i�^��m�v����$=��5gDj�ۺ�Z�d
\����#�K�W�(7�'x�ٰNy��	s�H��wsd�Tr�ÕZD���L4�����m#I��~�q]�7��BY��7
�ݞu��T��ʪ5�̿Vg���fa��6�CS1\���T~a�[�'�����N�Ba�Q�4k�����xN^~��9��Wϡ ������/����" H�"5�"�s��KW#�Q�aaj�G]r����i%������O,��ČN���Ŀ�?���}4�}�y�W���	�GE�N��}��G��>p֒Y��6�� $W�N���!	�U���*�H@AD
���[��;u�(�P�+����eK��o���G���I�Gy7dـ M[Z
0*�ucq(a�m��N�~M`��)軎�"5{���Ƀn)�#�`-K���x{�rAP�y"�!��*1�X��U`:�jxU��:� JɭcGXq��)���������-�V3Zق�A/>�L��l�Q瞣.�l:�VX�x6���(��H5�+�/Y&�{��z�yb��~!-�ذ������@�5�v��Rx����<v�Ĵ�N;�sUM�JuD����φF���l��Ls�A�0=t:��iI#_j��C�"�*�ر�؍H9���s�g�̵����^7����
F�D�O~��0w�m��<�Ĵ�0�,�_2�|����Vm�<Þ� (��8F�0N����&��� {\E�tMs�l%U�z��ǘZ��TD�HJ�ڒjq�F@f��z?@4A�^34?ޚ�t1N����Kr�m.��ˑ�wI���D2����5e(���v���
�Z�(��aO\��=�i�����x�gg4��%^Ƿ��PV�y�z�l��k>g&��:����n`芺��`��C�i���Zt;���7S)��)��1Go����7$�ק�K]'��<Ia�$�Ty@�4Y#�竡FX������&� �n�l�2pG��s�������m�/�s��r��X� �掷jF�EkǙy��Z����9AYqw�5y{�Q�d.T���K��eQf%��iZP��/�-��0P*E�8؅8|�4DA�DQ�";����Y@mFcns��ԃ��N��:9�Q�}v�����N�H�f��,���&�dD~)s��/ѵ��ହ��,;�ή}�o6�`)��ϴti��>�Z�L�=.����4�B�C&ч�ʠ�	���i�tc,Q]\�q�Y? ]?�e����ʰ��4fz�#�;t����?�z�.1�����0���\pԔ���:tj(K�aF�?�n��N����DE�'5�<<�1e�>Ь�(QO�	�o�5}/���{I~Ŵ���Y�Q0�1�2�Dh�x��t�4@��x��M���X�!�m�w��2��E�0g�,�����/P{"�:a�S{���"���b��cSO�q�L��{��1)��ѝ�v�V��v�χ�]ߡF������B����&�=�Xׁ\��q�g���8�%�lf�p^ʐ��&��Q�Z�j�8e�y��7¢q֔����Y�.��YE�۠O�Xl�b]�q�Utr%��ȷ/r�z���kڷ��	�������~'��Yn�
�QQ4*�䎜��'��h�����qEf�k�&钸�߹�i�8�ոˏC=��e�y�H6��m�{��9�yta'8�$���U�R���go�LM�Ƿ�BG�H�U�4k����ܑ��,X�{5���{"�M��!�DB�m�F4Ơ�O���IH�PcG�����&c�9&��,������$�6���7SId]6��P*t毇�x>����J�3zѣB�ԙ|Y��u��^C�����u?�z��~����׵N3��,D|�.v*X�Y%u��̶A�ǒ"�*�{W��1Z 2/2��@&l_c�y���ls餎y<-�J;83�ƶ�����/���O�c���ڿ]~v�A3{�H�fKO"��X���g;�@Oi���ݓ��q���s����J�MQ`�H����ܭJ����%���Ç�QuD6(�������:���?[	H,~�b�
�T�P��R��G�\͎�;�1x���%/������Iƿ��nw�����Ht����6�����������t�&}7���!Џ��n�+��0����ʦ#��ZP��)a�z��r-�I}��C�������,�-١�X�_�||�����#Tе�s5�e���>��Yg���k����2�͐�[��<��r�F\�q��+�����Z�d��>�@����4�U�b���jDb:����ؤ��_^��H1�]���]�f�Xw+�e���:?���7�!�Rfl@z�	�D�@-�.�fH=��;�Z�����ޟ�_�%!K��/ly��G4��r�ž�1O��O�Z�~<ף4C�'Q��Ї�S�t�=~��ϋ��8��m�E��p?��Џ=�Q�򑩌wxJ�Ė<����������Hr�c���g�ﵸl��kQ��c~���Q��Ϣ�fE�)+B/-�uL�y�Ԑ�iC�X�|;\�v��,�xjg)e�O���q;��'ͤ���� "���.ql��ǡO< ���
{"j�A��0�<�2i�Ƀ�N^�x�_��3      
      x������ � �     